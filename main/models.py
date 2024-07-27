from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length = 150)
    completed = models.BooleanField(default = False)

# python manage.py makemigrations
# python manage.py migrate
    
