from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreation(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreation, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'E-mail'
        self.fields['email'].widget.attrs['class'] = 'email'

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)