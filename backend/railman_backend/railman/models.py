from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=20) 

class Restaurant(models.Model):
    """Model representing a Expert."""
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=20)