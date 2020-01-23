from django.shortcuts import render
from django.views.generic import DetailView

from .models import Product


# class ProductInstance(DetailView):
#     model = Product
#     template_name = 'product/product_instance.html'
#
#     def get_context_data(self, **kwargs):
#         ctx = super(ProductInstance, self).get_context_data(**kwargs)
#         ctx['title'] = Product.objects.filter(pk=self.kwargs['pk']).first()
#         return ctx

def product_instance_view(request, pk):
    product = Product.objects.get(id=pk)

    data = {
        'product': product,
    }

    return render(request, 'product/product_instance.html', data)