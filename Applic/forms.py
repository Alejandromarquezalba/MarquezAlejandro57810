from django import forms
from .models import Client, Market, Worker


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





    