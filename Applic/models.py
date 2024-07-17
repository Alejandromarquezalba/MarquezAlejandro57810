from django.db import models

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