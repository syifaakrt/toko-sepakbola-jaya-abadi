from django.forms import ModelForm
from .models import Product
from django.utils.html import strip_tags

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
    def clean_title(self):
        title = self.cleaned_data["title"]
        return strip_tags(title)

    def clean_content(self):
        content = self.cleaned_data["content"]
        return strip_tags(content)
