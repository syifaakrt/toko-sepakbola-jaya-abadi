import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.core import serializers
from .forms import ProductForms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
# Create your views here.

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name")) 
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on' 
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

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
    json_data = [
        {
            "pk": str(product.id),
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "thumbnail": product.thumbnail,
            "category": product.category,
            "is_featured": product.is_featured,
            "user": product.user.id if product.user else None
        } for product in product_list
    ]
    return JsonResponse(json_data, safe=False)

def show_xml_byId(request, productId):
    try:
        product_list = Product.objects.filter(pk=productId)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type = "application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_byId(request, productId):
    try:
        product = Product.objects.select_related('user').get(pk=productId)
        data = {
            "pk": str(product.id),
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "thumbnail": product.thumbnail,
            "category": product.category,
            "is_featured": product.is_featured,
            "user_id": product.user.id if product.user else None,
            "user_username": product.user.username if product.user else None
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({"detail": "Product not found"}, status=404)
    
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

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Akun kamu berhasil dibuat! Silakan login ya 👋',
                    'redirect_url': reverse('main:login')
                })
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'message': 'Gagal membuat akun. Coba cek kembali data yang kamu isi.'
                })

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': f'Halo, {user.username}! Selamat datang kembali 👋',
                    'redirect_url': reverse("main:show_main"),
                })

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Username atau password salah. Coba lagi, ya!',
            })

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': "Kamu berhasil logout. Sampai jumpa lagi!",
                'redirect_url': reverse("main:login"),
            })

        return HttpResponseRedirect(reverse("main:login"))

    return JsonResponse({'success': False, 'message': 'Metode tidak diizinkan.'})

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