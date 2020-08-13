
from rest_framework import serializers

from restaurant.models import Restaurant, Toppings, Dish


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id', 'name')


class ToppingsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Toppings
        fields = ('url', 'id', 'name', 'price')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    toppings = serializers.SlugRelatedField(many=True, slug_field='name',
                                            queryset=Toppings.objects.all())

    class Meta:
        model = Dish
        fields = ('url', 'id', 'name', 'price', 'restaurant', 'category')

