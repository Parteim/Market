from django.shortcuts import render
from django.views.generic import DetailView, ListView

from cart.models import Cart
from products.models import Product


def home(request):
    if request.method == 'POST':
        product_name = request.POST.get('product')
        product_object = Product.objects.get(name=product_name)
        print(f'================={type(product_object)}===========')
        product = Cart(user=request.user, product=product_object)
        product.save()

    products = Product.objects.all()
    data = {
        'title': 'ATOM',
        'products': products,
    }

    return render(request, 'main/index.html', data)
