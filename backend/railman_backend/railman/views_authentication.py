from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

import json

from railman.models import User
from railman.serializers import UserSerializer
from railman.models import Restaurant
from railman.serializers import RestaurantSerializer

####################   Authentication - register 

@api_view(['POST'])
def register(request):
	if request.method == 'POST':
		new_user_data = JSONParser().parse(request)
		user_email = new_user_data['email']
		user_role = new_user_data['role']
		if user_email is not None and user_role is not None:	
			customers = User.objects.all()
			customer = customers.filter(email__icontains=user_email) 		
			experts = Restaurant.objects.all()				
			expert = experts.filter(email__icontains=user_email) 
			if(len(customer) == 0 and len(expert) == 0):
				if (user_role == "user" or user_role == "restaurant"):
					# TODO - password hashing
					serializer = None
					if user_role == "user":
						serializer = UserSerializer(data=new_user_data)
					if user_role == "restaurant":
						# TODO - handle expertise details
						serializer = RestaurantSerializer(data=new_user_data)
					if serializer.is_valid():
						serializer.save()
						return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
					return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
				else:
					return JsonResponse({'message': 'Role Not supported!'}, status=status.HTTP_204_NO_CONTENT)       	
			else:
				return JsonResponse({'message': 'User already exists!'}, status=status.HTTP_204_NO_CONTENT)       
		else:
			return JsonResponse({'message': 'Check the registration details again!'}, status=status.HTTP_204_NO_CONTENT)       
