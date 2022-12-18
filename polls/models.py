from django.db import models


class MyTable(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to="polls/static", blank=True)


class Animal (models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

# Create your models here.
