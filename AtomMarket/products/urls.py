from django.urls import path
from . import views

urlpatterns = [
    # path('product-instance/<int:pk>/', views.ProductInstance.as_view(), name='product-instance'),
    path('product-instance/<int:pk>/', views.product_instance_view, name='product-instance'),
]

