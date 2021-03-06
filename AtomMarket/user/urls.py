from django.urls import path
from django.contrib.auth import views

from .forms import CustomUserCreation
from . import views as sign_up_views

urlpatterns = [
    path('sign_up/', sign_up_views.signup, name='sign-up'),
    path('sign_in/', views.LoginView.as_view(template_name='user/sign_in.html',), name='sign-in'),
]