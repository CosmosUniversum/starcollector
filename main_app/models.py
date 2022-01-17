from django.db import models
from django.urls import reverse

# Create your models here.

class Star(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  constellation = models.CharField(max_length=100)
  distance = models.IntegerField()

  def __str__(self):
      return self.name

  def get_absolute_url(self):
      return reverse("stars_detail", kwargs={"star_id": self.id})


class Exoplanet(models.Model):
  name = models.CharField(max_length=100)
  atmosphere = models.CharField(max_length=200)
  star = models.ForeignKey(Star, on_delete=models.CASCADE)

  def __str__(self):
      return self.name

class Photo(models.Model):
  url = models.CharField(max_length=250)
  star = models.OneToOneField(Star, on_delete=models.CASCADE)

  def __str__(self):
      return f"Photo for star_id: {self.star_id} @{self.url}."