
from rest_framework import serializers

from restaurant.models import Restaurant, Toppings, Dish


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('url', 'id', 'name', 'city')


class ToppingsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Toppings
        fields = ('url', 'id', 'name', 'price')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    toppings = serializers.SlugRelatedField(many=True, slug_field='name',
                                            queryset=Toppings.objects.all())
    restaurant = serializers.SlugRelatedField(slug_field='name',
                                              queryset=Restaurant.objects.all())
    category = serializers.CharField(source='get_category_display')

    class Meta:
        model = Dish
        fields = ('url', 'id', 'name', 'price', 'restaurant', 'category', 'toppings')

