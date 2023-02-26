from django.urls import path
#from django.conf.urls import url 
from . import views
from . import views_authentication

urlpatterns = [
    path('', views.home, name='home'),
    path('api/core/user/', views.UserList.as_view()),
    path('api/core/user/<int:pk>/', views.UserDetail.as_view()), 
    path('api/authentication/registration/', views_authentication.register),
    path('api/authentication/login/', views_authentication.login),
    path('api/restaurants/city/', views.RestaurantList.as_view()), 
    path('api/menu/', views.MenuList.as_view()), 
]

