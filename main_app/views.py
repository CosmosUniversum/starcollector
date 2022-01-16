from dataclasses import field
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Star
from main_app import models

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
  return render(request, 'stars/detail.html', {'star': star})

class StarCreate(CreateView):
  model = Star
  fields = '__all__'

class StarUpdate(UpdateView):
  model = Star
  fields = '__all__'

class StarDelete(DeleteView):
  model = Star
  success_url = '/stars/'