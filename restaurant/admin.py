from django.contrib import admin

from restaurant.models import Restaurant, Toppings, Dish

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')


@admin.register(Toppings)
class ToppingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'restaurant',
                    'toppings_list', 'category')

    def toppings_list(self, obj):
        return ', '.join([str(t) for t in obj.toppings.all()])

