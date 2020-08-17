from django.shortcuts import render

import django_filters.rest_framework

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAdminUser

from rest_framework import generics, filters

from restaurant.models import Restaurant, Toppings, Dish


from api.serializers import RestaurantSerializer, ToppingsSerializer, DishSerializer

#Create your views here.


class RestaurantListApiView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'city']
    ordering_fields = ['name', 'city']


class RestaurantApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminUser]


class ToppingsListApiView(generics.ListAPIView):
    queryset = Toppings.objects.all()
    serializer_class = ToppingsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'price']


class ToppingsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toppings.objects.all()
    serializer_class = ToppingsSerializer
    permission_classes = [IsAdminUser]


class DishListApiView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'restaurant__name', 'toppings__name']
    ordering_fields = ['name', 'restaurant__name', 'category']


class DishApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminUser]

