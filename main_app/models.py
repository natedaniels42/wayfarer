from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from time import strftime
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    image = models.CharField(max_length=500)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)