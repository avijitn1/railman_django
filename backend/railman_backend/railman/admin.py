from django.contrib import admin
from .models import User, RestaurantOwner, Restaurant, Menu
# Register your models here.

admin.site.register(User)
admin.site.register(RestaurantOwner)
admin.site.register(Restaurant)
admin.site.register(Menu)
