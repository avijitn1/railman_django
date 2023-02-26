from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

import json

from railman.models import User
from railman.serializers import UserSerializer
from railman.models import RestaurantOwner
from railman.serializers import RestaurantOwnerSerializer

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
			experts = RestaurantOwner.objects.all()				
			expert = experts.filter(email__icontains=user_email) 
			if(len(customer) == 0 and len(expert) == 0):
				if (user_role == "user" or user_role == "restaurant"):
					# TODO - password hashing
					serializer = None
					if user_role == "user":
						serializer = UserSerializer(data=new_user_data)
					if user_role == "restaurant":
						# TODO - handle expertise details
						serializer = RestaurantOwnerSerializer(data=new_user_data)
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

@api_view(['POST'])
def login(request):
	if request.method == 'POST':
		user_data = JSONParser().parse(request)
		user_email = user_data['email']
		user_password = user_data['password']
		user_role = user_data['role']
		print(user_email, user_password, user_role)
		if user_email is not None and user_role is not None and user_password is not None:	
			# TODO - password hashing
			customers = User.objects.all()
			customer = customers.filter(email__icontains=user_email) 	
			customer = customer.filter(password__icontains=user_password) 	
			experts = RestaurantOwner.objects.all()				
			expert = experts.filter(email__icontains=user_email) 
			expert = expert.filter(password__icontains=user_password) 
			if(len(customer) != 0 or len(expert) != 0):
				if (user_role == "user" or user_role == "restaurant"):
					if user_role == "user":
						serializer = UserSerializer(customer, many=True)
					if user_role == "restaurant":
						serializer = RestaurantOwnerSerializer(expert, many=True)
					return JsonResponse(serializer.data, safe=False)
				else:
					return JsonResponse({'statusText': 'Role Not supported!'}, status=status.HTTP_204_NO_CONTENT)       	
			else:
				return JsonResponse({'statusText': 'Check the login details again!'}, status=status.HTTP_204_NO_CONTENT)       
		else:
			return JsonResponse({'statusText': 'Check the login details again!'}, status=status.HTTP_204_NO_CONTENT)  