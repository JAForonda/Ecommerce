from django.db import models

from datetime import date
from django.utils import timezone
# # Create your models here.
class order (models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    cart = models.CharField(max_length=200, default='None')
    payment_id = models.CharField(max_length=200, default = 'None')
    user_id = models.CharField(max_length=200, default = 'None')
    first_name = models.CharField(max_length=200, default = 'None')
    last_name = models.CharField(max_length=200, default = 'None')
    email = models.CharField(max_length=300, default = 'None')
    address = models.CharField(max_length=400, default = 'None')
    country = models.CharField(max_length=50, default= 'None')
    state = models.CharField(max_length=50, default = 'None')
    city = models.CharField(max_length=50, default='None')
    total = models.FloatField(default=0)
    status = models.CharField(max_length=30, default = 'None')
    is_ordered= models.BooleanField(default=False)
    created_date = models.DateTimeField(default = timezone.now())
    updatd_date = models.DateTimeField(default = timezone.now())
