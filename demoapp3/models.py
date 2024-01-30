from django.db import models

class reg(models.Model):
    name = models.CharField(max_length=200)
    age =models.IntegerField()
    email=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
