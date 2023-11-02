from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    currency = models.CharField(max_length=20)
    balance = models.IntegerField()


    def __str__(self):
        return self.name

