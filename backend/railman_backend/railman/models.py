from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.CharField(max_length=20, blank=False) 

class RestaurantOwner(models.Model):
    """Model representing a Expert."""
    name = models.CharField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.CharField(max_length=20, blank=False)

class Restaurant(models.Model):
    name = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=200, blank=False, default='Indian Restaurant')
    min_order = models.IntegerField(blank=False, default=100)

class Menu(models.Model):
    restaurantId = models.ForeignKey('Restaurant', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(blank=False)
    description = models.CharField(max_length=200, blank=False)
