from django.contrib.auth.models import User
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView


from restaurant.forms import SignUpForm


class HomeView(TemplateView):
    template_name = 'home.html'


class RegisterView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']


            User.objects.create_user(username=username,
                                         password=password1,
                                         email=email)

            return redirect(reverse_lazy('home'))
        return render(request, 'register.html', {'form': form})


