from django.db import models
from django.utils import timezone

class Task(models.Model):
    name = models.CharField(max_length = 32,default ="")
    completed = models.BooleanField(default=False)
    date_time = models.DateTimeField(default=timezone.now)

    
class User(models.Model):
    pass