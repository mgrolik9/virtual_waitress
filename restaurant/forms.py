from django import forms
from django.contrib.auth.models import User

from django.core import validators
from django.forms import PasswordInput
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100, validators=[validators.validate_email])
    password1 = forms.CharField(max_length=10, widget=PasswordInput)
    password2 = forms.CharField(max_length=10, widget=PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Password is incorrect')
