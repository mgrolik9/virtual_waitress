from django import template
from django.http import request

register = template.Library()

from restaurant.models import Restaurant


@register.simple_tag
def restaurant_registered():
    return Restaurant.objects.all().count()


