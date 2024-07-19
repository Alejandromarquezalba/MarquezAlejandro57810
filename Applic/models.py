from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Market(models.Model):
    money = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.money}'

class Client(models.Model):
    money = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.money}'

class Worker(models.Model):
    pay = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.pay}'
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to='avatares', default='media/avatares/default.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.imagen}'