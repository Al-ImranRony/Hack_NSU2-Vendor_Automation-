from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    company_name = forms.CharField(max_length=100)
    cell = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'company_name', 'cell', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    company_name = forms.CharField(max_length=100)
    cell = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'company_name', 'cell']


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    company_name = forms.CharField(max_length=100)
    cell = forms.IntegerField()

    class Meta:
        model = Profile
        fields = ['email', 'company_name', 'cell']