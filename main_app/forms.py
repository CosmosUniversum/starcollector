from django.forms import ModelForm
from .models import Exoplanet

class ExoplanetForm(ModelForm):
  class Meta:
    model = Exoplanet
    fields = ['name', 'atmosphere']