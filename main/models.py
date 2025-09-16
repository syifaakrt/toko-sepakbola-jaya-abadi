import uuid
from django.db import models

# Create your models here.
class Product (models.Model):
    CATEGORY_CHOICES = [
        ('ball', 'Bola'),
        ('shoes', 'Sepatu Bola'),
        ('jersey', 'Jersey'),
        ('gloves', 'Sarung Tangan'),
        ('accessories', 'Aksesoris'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField
    description = models.TextField(max_length=500)
    thumbnail = models.URLField((""), max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='bola')
    is_featured = models.BooleanField(default=False)