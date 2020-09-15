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
from restaurant.forms import SignUpForm, RestaurantForm


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
            return redirect(reverse_lazy('home'))

        response = 'Account not exist'
        return render(request, 'login.html', {'response': response})


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('home'))


class CreateRestaurantView(LoginRequiredMixin, FormView):

    login_url = '/login/'
    template_name = 'restaurant_form.html'
    form_class = RestaurantForm
    success_url = '/'

    def form_valid(self, form):
        owner = self.request.user
        new_restaurant = Restaurant.objects.create(owner=owner,
                                                   name=form.cleaned_data['name'],
                                                   city=form.cleaned_data['city'],
                                                   image=form.cleaned_data['image'])
        new_restaurant.save()
        return super().form_valid(form)


