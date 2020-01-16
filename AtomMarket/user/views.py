from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import CustomUserCreation


def signup(request):

    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('email')
            messages.success(request, f'User {name} has been successfully registered')
            return redirect('sign_up')

    else:
        form = CustomUserCreation()

    return render(request, 'user/sign_up.html', {'form': form, 'title': 'Register'})
