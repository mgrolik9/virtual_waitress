
from django.urls import path


from api.views import RestaurantListApiView, RestaurantApiView, ToppingsListApiView, \
    ToppingsApiView, DishListApiView, DishApiView

urlpatterns = [
    path('api/restaurants', RestaurantListApiView.as_view(), name="restaurants-api"),
    path('api/restaurants/<int:pk>', RestaurantApiView.as_view(), name="restaurant-detail"),
    path('api/toppings', ToppingsListApiView.as_view(), name="toppings-api"),
    path('api/toppings/<int:pk>', ToppingsApiView.as_view(), name="topping-detail"),
    path('api/dish', DishListApiView.as_view(), name="dish-api"),
    path('api/dish/<int:pk>', DishApiView.as_view(), name="dish-detail")
]