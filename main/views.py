import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .forms import ProductForms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    product_list = Product.objects.all()
    return render(request, "main.html", {'product_list':product_list, 'last_login': request.COOKIES.get('last_login', 'Never')})

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
    
@login_required(login_url='/login')
def add_product(request):
    form = ProductForms(request.POST or None)
    if (form.is_valid and request.method == "POST"):
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {"form":form}
    return render(request, 'add_product.html', context)

@login_required(login_url='/login')
def show_product(request, productId):
    product = get_object_or_404(Product, pk=productId)
    return render(request, 'product_details.html', {'product':product})

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, productId):
    product = get_object_or_404(Product, pk=productId)
    form = ProductForms(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, productId):
    product = get_object_or_404(Product, pk=productId)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))