from django.shortcuts import render
from django.views.generic import DetailView

from cart.models import Cart
from .models import Product


def product_instance_view(request, pk):

    product = Product.objects.get(id=pk)

    data = {
        'product': product,
    }

    if request.method == 'POST':
        product_save = Cart(user=request.user, product=product)
        product_save.save()

    return render(request, 'product/product_instance.html', data)