from django.db import models


# Create your models here.
class Store(models.Model):
    id = models.IntegerField(unique = True, primary_key= True, blank=False)
    category_id = models.IntegerField(blank=False)
    product_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    images = models.CharField(max_length=100)
    stock = models.IntegerField()
    is_available = models.BooleanField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
class variations(models.Model):
    product = models.ForeignKey(Store, on_delete=models.CASCADE)
    small = models.BooleanField(default=False)
    medium = models.BooleanField(default=False)
    large = models.BooleanField(default=False)
    extraL = models.BooleanField(default=False)