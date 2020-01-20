from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreation


def signup(request):

    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('email')
            messages.success(request, f'User {name} has been successfully registered')
            return redirect('sign_in')

    else:
        form = CustomUserCreation()

    return render(request, 'user/sign_up.html', {'form': form, 'title': 'Register'})


@login_required
def cart(request):

    return render(request, 'main/cart.html')
