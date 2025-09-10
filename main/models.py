from django.db import models

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField
    description = models.TextField(max_length=500)
    thumbnail = models.URLField((""), max_length=200)
    category = models.CharField
    is_featured = models.BooleanField