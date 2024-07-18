from django import forms
from .models import Client, Market, Worker
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['money', 'product']

class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = ['money', 'client']

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['pay', 'hours']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




    