
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import json

from railman.models import User, Menu, Restaurant, RestaurantOwner
from railman.serializers import UserSerializer, MenuSerializer, RestaurantSerializer

class UserList(APIView):
    """
    List all customers, or create a new customer.
    """
    def get(self, request, format=None):
        customers = User.objects.all()
        serializer = UserSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a customer instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = UserSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = UserSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RestaurantList(APIView):
    """
    List all customers, or create a new customer.
    """
    def get(self, request, format=None):
        restuarants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restuarants, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request_data = JSONParser().parse(request)
        city = request_data['city']

        restaurants = Restaurant.objects.all()
        filteredRestaurants = restaurants.filter(city__icontains=city) 		 
        serializer = RestaurantSerializer(filteredRestaurants, many=True)
        return JsonResponse(serializer.data, safe=False)

class MenuList(APIView):
    """
    List all customers, or create a new customer.
    """
    def get(self, request, format=None):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request_data = JSONParser().parse(request)
        name = request_data['name']

        restaurants = Restaurant.objects.all()
        filteredRestaurants = restaurants.filter(name=name).values_list('id')
        #restaurants_filtered = filteredRestaurants.filter(city=city)
        if filteredRestaurants:
            restaurant_id = filteredRestaurants[0][0]
        else:
            restaurant_id = -1
       
        menus = Menu.objects.all()
        menuList = menus.filter(restaurantId=restaurant_id)
        serializer = MenuSerializer(menuList, many=True)
        return JsonResponse(serializer.data, safe=False)

# Create your views here.
def home(request):
    return Response('Hello World')