from django.contrib.auth.models import User
from django.db import models


# Create your models here.

DISH_CATEGORIES = {
    (1, 'dinner'),
    (2, 'lunch'),
    (3, 'starters'),
    (4, 'drinks'),
    (5, 'alcohol'),
    (6, 'other')
}


class Restaurant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Nazwa restauracji')
    city = models.CharField(max_length=100, verbose_name='Nazwa miasta', default='')
    image = models.ImageField(default='default_picture/default.JPG')

    def __str__(self):
        return self.name + ',' + self.city


class Toppings(models.Model):
    name = models.CharField(max_length=100, verbose_name='Składniki')
    price = models.IntegerField(default=0, verbose_name='Cena za dodatek')

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa dania/napoju')
    price = models.IntegerField(verbose_name='Cena za danie')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Toppings, related_name='dish_toppings_set', blank=True)
    category = models.IntegerField(choices=DISH_CATEGORIES, verbose_name='Kategoria dania')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



