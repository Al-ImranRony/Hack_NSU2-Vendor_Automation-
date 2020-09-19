from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    company_name = forms.CharField(max_length=100)
    cell = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'company_name', 'cell', 'password1', 'password2']