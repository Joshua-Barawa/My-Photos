from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    profile = forms.ImageField()
    email = forms.EmailField(max_length=200)
    bio = forms.TextInput()

    class Meta:
        model = User
        fields = ('username', 'profile', 'email', 'bio', 'password1', 'password2')

