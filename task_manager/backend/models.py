from django.db import models

class Task(models.Model):
    name = models.CharField(max_length = 32,default ="")

    
class User(models.Model):
    pass