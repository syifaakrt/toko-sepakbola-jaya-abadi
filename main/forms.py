from django.forms import ModelForm
from .models import Product

class ProductForms(ModelForm):
    
    class Meta:
        model = Product
        fields = ("name", "price", "description", "thumbnail", "category", "is_featured")
