from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from restaurant.models import Restaurant
from restaurant.forms import SignUpForm, RestaurantForm, AddMenuForm


class HomeView(TemplateView):
    template_name = 'home.html'


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = 'login/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']

        User.objects.create_user(username=username, email=email, password=password1)
        return super().form_valid(form)


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(username=request.POST.get('login'),
                            password=request.POST.get('password'))

        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('home-restaurant'))

        response = 'Account not exist'
        return render(request, 'login.html', {'response': response})


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('home-restaurant'))


class CreateRestaurantView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = RestaurantForm()
        owners = [restaurant.owner for restaurant in Restaurant.objects.all()]

        return render(request, 'restaurant_form.html', locals())

    def post(self, request):
        form = RestaurantForm(request.POST)

        if form.is_valid():
            new_restaurant = Restaurant.objects.create(owner=request.user,
                                                       name=form.cleaned_data['name'],
                                                       city=form.cleaned_data['city'])
            new_restaurant.image = form.cleaned_data['image']
            new_restaurant.save()
            return redirect(reverse_lazy('restaurant'))


class AddMenuView(LoginRequiredMixin, FormView):
    login_url = '/login/'

    template_name = 'add_menu.html'
    form_class = AddMenuForm
    success_url = 'add_menu/'
