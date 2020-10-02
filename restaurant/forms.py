from django import forms
from django.contrib.auth.models import User

from django.core import validators
from django.forms import PasswordInput, ModelForm
from django.core.exceptions import ValidationError

from restaurant.models import Restaurant, Dish


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100, validators=[validators.validate_email])
    password1 = forms.CharField(max_length=10, widget=PasswordInput)
    password2 = forms.CharField(max_length=10, widget=PasswordInput)

    def clean_email(self):
        data = self.cleaned_data['email']
        duplicate_users = User.objects.filter(email=data)
        if duplicate_users.exists():
            raise ValidationError('Email already exists')
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        duplicate_users = User.objects.filter(username=data)
        if duplicate_users.exists():
            raise ValidationError('User already exists')
        return data

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('Password is incorrect')


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ['owner']


class AddMenuForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ['restaurant', 'toppings']
