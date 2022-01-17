from dataclasses import field
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Star
from main_app import models
from .forms import ExoplanetForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def stars_index(request):
  stars = Star.objects.all()
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
  fields = '__all__'

class StarUpdate(UpdateView):
  model = Star
  fields = '__all__'

class StarDelete(DeleteView):
  model = Star
  success_url = '/stars/'