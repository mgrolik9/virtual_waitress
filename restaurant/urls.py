from django.urls import path
from django.contrib.auth import views as auth_views

from restaurant.views import HomeView, RegisterView, CreateRestaurantView, AddMenuView,\
    AddToppingsView

urlpatterns = [
    path('home_restaurant/', HomeView.as_view(), name="home-restaurant"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('create_restaurant/', CreateRestaurantView.as_view(), name="restaurant"),
    path('add_menu/', AddMenuView.as_view(), name="add-menu"),
    path('add_toppings/', AddToppingsView.as_view(), name="add-toppings")
]
