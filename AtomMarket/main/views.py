from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.db.models import Q
from django.http import HttpResponseRedirect


from cart.models import Cart
from products.models import Product


def home(request):
    products = Product.objects.all()
    data = {
        'title': 'ATOM',
        'products': products,
    }

    if request.method == 'POST':
        product_name = request.POST.get('product')
        product_object = Product.objects.get(name=product_name)
        print(f'================={type(product_object)}===========')
        product = Cart(user=request.user, product=product_object)
        product.save()

    return render(request, 'main/index.html', data)


def pc_page(request):
    if request.method == 'POST':
        product_name = request.POST.get('product')
        product_object = Product.objects.get(name=product_name)
        print(f'================={type(product_object)}===========')
        product = Cart(user=request.user, product=product_object)
        product.save()

    products = Product.objects.all().filter(type_of_product='PC')
    data = {
        'title': 'ATOM',
        'products': products,
    }

    return render(request, 'main/index.html', data)


def tv_page(request):
    if request.method == 'POST':
        product_name = request.POST.get('product')
        product_object = Product.objects.get(name=product_name)
        print(f'================={type(product_object)}===========')
        product = Cart(user=request.user, product=product_object)
        product.save()

    products = Product.objects.all().filter(type_of_product='TV')
    data = {
        'title': 'ATOM',
        'products': products,
    }

    return render(request, 'main/index.html', data)


def mobile_phone_page(request):
    if request.method == 'POST':
        product_name = request.POST.get('product')
        product_object = Product.objects.get(name=product_name)
        print(f'================={type(product_object)}===========')
        product = Cart(user=request.user, product=product_object)
        product.save()

    products = Product.objects.all().filter(type_of_product='MobilePhone')
    data = {
        'title': 'ATOM',
        'products': products,
    }

    return render(request, 'main/index.html', data)


def location_page(request):
    data = {
        'title': 'Location',
    }

    return render(request, 'main/location.html', data)


def search(request):
    template = 'main/index.html'
    search_value = request.GET.get('search')
    if search_value == 'BAN':
        template = 'main/ban.html'
    products = Product.objects.filter(Q(name__icontains=search_value))

    data = {
        'title': 'ATOM',
        'products': products,
    }

    return render(request, template, data)


def add_in_cart(request):
    product_name = request.POST.get('product')
    product_object = Product.objects.get(name=product_name)
    print(f'================={type(product_object)}===========')
    product = Cart(user=request.user, product=product_object)
    product.save()

    return redirect('')