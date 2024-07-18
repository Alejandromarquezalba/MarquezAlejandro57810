from django import forms
from .models import Client, Market, Worker
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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

class EditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Nombre', max_length=20, required=True)
    last_name = forms.CharField(label='Apellido', max_length=20, required=True)

    class Meta:
        model = User
        fields = ['email','first_name','last_name']


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    