from django.db import models
from django.forms import PasswordInput

# Create your models here.
class userProfile (models.Model):
    userId = models.CharField(primary_key=True, max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
class account (models.Model):
    userId = models.CharField(primary_key=True, max_length=200)
    password = models.CharField(max_length=300)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    userName = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    is_active = models.BooleanField(default=False)
