from django.urls import path
from . import views
from . import views_authentication

urlpatterns = [
    path('', views.home, name='home'),
    path('api/core/user/', views.UserList.as_view()),
    path('api/core/user/<int:pk>/', views.UserDetail.as_view()), 
    path('api/authentication/registration/', views_authentication.register),  
]

