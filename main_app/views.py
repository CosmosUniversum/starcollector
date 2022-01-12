from django.shortcuts import render

class Star:
  def __init__(self, name, constellation, type, distance):
      self.name = name
      self.constellation = constellation
      self.type = type
      self.distance = distance

stars = [
  Star('Vega', 'Lyra', 'main-sequence', '25'),
  Star('Betelgeuse', 'Orion', 'Red Supergiant', '500-600'),
  Star('Antares', 'Scorpius', 'Red Supergiant', '550')
]
# Create your views here.
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def stars_index(request):
  return render(request, 'stars/index.html', {'stars': stars})