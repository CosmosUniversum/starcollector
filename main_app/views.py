from dataclasses import field
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Exoplanet, Star, Photo
from main_app import models
from .forms import ExoplanetForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'starcollector'

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def stars_index(request):
  stars = Star.objects.filter(user=request.user)
  return render(request, 'stars/index.html', {'stars': stars})

def stars_detail(request, star_id):
  star = Star.objects.get(id=star_id)
  exoplanet_form = ExoplanetForm()
  return render(request, 'stars/detail.html', {'star': star, 'exoplanet_form': exoplanet_form})

def add_exoplanet(request, star_id):
  form = ExoplanetForm(request.POST)
  if form.is_valid():
    new_exoplanet = form.save(commit=False)
    new_exoplanet.star_id = star_id
    new_exoplanet.save()
    return redirect('stars_detail', star_id=star_id)

class StarCreate(CreateView):
  model = Star
  fields = ['name', 'type', 'constellation', 'distance']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class StarUpdate(UpdateView):
  model = Star
  fields = '__all__'

class StarDelete(DeleteView):
  model = Star
  success_url = '/stars/'

class ExoplanetUpdate(UpdateView):
  model = Exoplanet
  fields = ['name', 'atmosphere']
  success_url = '/stars/'


class ExoplanetDelete(DeleteView):
  model = Exoplanet
  success_url = '/stars/'

def add_photo(request, star_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, star_id=star_id)
      star_photo = Photo.objects.filter(star_id=star_id)
      if star_photo.first():
        star_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
    return redirect('stars_detail', star_id=star_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('stars_index')
    else:
      error_message = 'Invalid Signup, try again.'
  form = UserCreationForm()
  context = {'form': form, 'error message': error_message}
  return render(request, 'signup.html', context)