from typing import Any
from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length = 150)
    completed = models.BooleanField(default = False)

    
class Movie(models.Model):
    title = models.CharField(max_length = 100)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='movies')
    
    
    

# python manage.py makemigrations
# python manage.py migrate
    
