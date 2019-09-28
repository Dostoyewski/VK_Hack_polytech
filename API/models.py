from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


class Acc(models.Model):
    #Неизменяемые
    events_registered = models.CharField(max_length=1000, blank=True)
    karma = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Изменяемые
    bio = models.TextField(max_length=500, blank=True, default='Не заполнено')
    location = models.CharField(max_length=30, default='Не указан')
    birth_date = models.DateField(null=True, blank=True)
    vorname = models.CharField(max_length=20, blank=True)
    nachname = models.CharField(max_length=50, blank=True)
    urlVK = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(null=False, blank=True, unique=True)

    def __str__(self):  
        return "%s's profile" % self.user