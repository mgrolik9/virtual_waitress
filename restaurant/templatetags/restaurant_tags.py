from django import template
from django.http import request

register = template.Library()

from restaurant.models import Restaurant, Dish


@register.inclusion_tag('registered_restaurant.html')
def registered_restaurant(user):
    restaurant = Restaurant.objects.get(owner=user)
    dishes = Dish.objects.filter(restaurant=restaurant).order_by('-date')[:2]
    return {'dishes': dishes}


