from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, blank=False)
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    Image = models.CharField(max_length=100)
    Slug = models.CharField(max_length=100)
