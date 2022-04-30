from django.db import models
from store.models import Store
import secrets
from checkout.utils import custom_id
 
# Create your models here.
 
class Cart(models.Model):
    cart_id = models.CharField(primary_key=True, unique='True', max_length=200, default=custom_id)
    user_id = models.CharField(max_length=200, default='none')
    active = models.BooleanField(default=False)
    date_added = models.DateField()
 
    def __str__(self):
        return self.cart_id
 
 
class CartItem(models.Model):
    user = models.CharField(max_length= 200)
    product = models.IntegerField()
    cart    = models.CharField(max_length=200)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
 
    def sub_total(self):
        return self.product.price * self.quantity
 
    def __unicode__(self):
        return self.product