from django.shortcuts import render

import django_filters.rest_framework

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAdminUser

from rest_framework import generics, filters

from restaurant.models import Restaurant, Toppings, Dish


from api.serializers import RestaurantSerializer, ToppingsSerializer, DishSerializer

#Create your views here.


class RestaurantListApiView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class RestaurantApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminUser]
