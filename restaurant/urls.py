from django.urls import path


from restaurant.views import HomeView, RegisterView, LoginView, CreateRestaurantView, Logout, AddMenuView,\
    AddToppingsView

urlpatterns = [
    path('home_restaurant/', HomeView.as_view(), name="home-restaurant"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('create_restaurant/', CreateRestaurantView.as_view(), name="restaurant"),
    path('add_menu/', AddMenuView.as_view(), name="add-menu"),
    path('add_toppings/', AddToppingsView.as_view(), name="add-toppings")
]
