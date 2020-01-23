from django.shortcuts import render

# from .models import Cart


def cart(request):
    data = {
        'title': 'ATOM cart',
    }

    return render(request, 'cart/cart.html', data)
