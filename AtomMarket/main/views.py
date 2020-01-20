from django.shortcuts import render


def home(request):

    return render(request, 'main/index.html', {'title': 'ATOM'})


def cart(request):

    return render(request, 'main/cart.html', {'title': 'ATOM cart'})
