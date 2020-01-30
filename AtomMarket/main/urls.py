from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pc-page/', views.pc_page, name='pc-page'),
    path('tv-page/', views.tv_page, name='tv-page'),
    path('mobile-phone-page/', views.mobile_phone_page, name='mobile-phone-page'),
    path('location-page/', views.location_page, name='location-page'),
    path('search/', views.search, name='search'),
    path('add-in-cart/', views.add_in_cart, name='add-in-cart'),
]
