from django.shortcuts import render

from .models import Cart


def cart(request):
    if request.method == 'POST':

        try:
            product_id = request.POST.get('product')

            product_obj = Cart.objects.get(pk=product_id)

            print(f'=========================={product_obj}=======================')
            product_obj.delete()
        except:
            pass

    data = {
        'title': 'ATOM cart',
    }

    return render(request, 'cart/cart.html', data)
