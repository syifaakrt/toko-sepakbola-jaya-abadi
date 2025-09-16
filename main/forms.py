from django.forms import ModelForm
from .models import Product

class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = ("name", "price", "description", "thumbnail", "category", "is_featured")
        labels = {
            "name":"Nama Produk",
            "price":"Harga",
            "description":"Deskripsi Produk",
            "category": "Kategori",
            "is_featured":"Unggul",
            "thumbnail": "Thumbnail:",
        }
