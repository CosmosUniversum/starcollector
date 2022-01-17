from django.contrib import admin
from .models import Star, Exoplanet, Photo

# Register your models here.
admin.site.register(Star)
admin.site.register(Exoplanet)
admin.site.register(Photo)