from django.db import models


from restaurant.models import Restaurant, Dish, Toppings

#Create your models here.


#class Basket(models.Model):
  #  dishes = models.ManyToManyField(Dish, related_name='basket_dish_set')
   # additional_toppings = models.ManyToManyField(Toppings, related_name='basket_toppings_set', blank=True)

   # def __str__(self):
    #    return 'basket ' + self.pk


#class Order(models.Model):
  #  table = models.IntegerField(verbose_name='Numer stolika')
   # basket = models.OneToOneField(Basket, on_delete=models.CASCADE)
  #  comment = models.CharField(max_length=100, verbose_name='Komenatarz do zamówienia', blank=True)
   # restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
   # date = models.DateField(auto_now_add=True)

   # def __str__(self):
    #    return self.restaurant.name

#migracja trzeba