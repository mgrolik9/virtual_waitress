
from django.urls import path


from api.views import RestaurantListApiView, RestaurantApiView

urlpatterns = [
    path('api/restaurants', RestaurantListApiView.as_view(), name="restaurants-api"),
    path('api/restaurants/<int:pk>', RestaurantApiView.as_view(), name="one-restaurant-api")
]