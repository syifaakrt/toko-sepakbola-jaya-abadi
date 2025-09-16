from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from django.http import HttpResponse
from django.core import serializers
from .forms import ProductForms

# Create your views here.

def show_main(request):
    product_list = Product.objects.all()
    return render(request, "main.html", {'product_list':product_list})

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type = "application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type = "application/json")

def show_xml_byId(request, productId):
    try:
        product_list = Product.objects.filter(pk=productId)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type = "application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_byId(request, productId):
    try:
        product_list = Product.objects.get(pk=productId)
        json_data = serializers.serialize("json", [product_list])
        return HttpResponse(json_data, content_type = "application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def add_product(request):
    form = ProductForms(request.POST or None)
    if (form.is_valid and request.method == "POST"):
        form.save()
        return redirect('main:show_main')
    
    context = {"form":form}
    return render(request, 'add_product.html', context)

def show_product(request, productId):
    product = get_object_or_404(Product, pk=productId)
    return render(request, 'product_details.html', {'product':product})
