from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreation(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreation, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'email'
        self.fields['password1'].widget.attrs['class'] = 'password'

        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)