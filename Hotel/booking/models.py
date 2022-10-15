from pyexpat import model
from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=30)
    description= models.CharField(max_length=100)
    location= models.CharField(max_length=20)
    type = models.CharField(max_length = 30)
    rating= models.CharField(max_length=10)
    image=models.ImageField()
