from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() #=> auth.User
        fields = ('username', 'email',
                'first_name', 'last_name',)
