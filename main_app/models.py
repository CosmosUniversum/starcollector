from django.db import models

# Create your models here.

class Star(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  constellation = models.CharField(max_length=100)
  distance = models.IntegerField()

  def __str__(self):
      return self.name