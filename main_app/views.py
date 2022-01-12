from django.shortcuts import render
from .models import Star

# Create your views here.
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def stars_index(request):
  stars = Star.objects.all()
  return render(request, 'stars/index.html', {'stars': stars})