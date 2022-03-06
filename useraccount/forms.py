from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'name': '',
            'description': "",
            'location': "",
            'category': "",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", "placeholder":"Image Name"}),
            'description': forms.TextInput(attrs={'class': "form-control", "placeholder": "Describe Image"}),
            'location': forms.Select(attrs={'class': "form-control", "placeholder": "Describe Image"}),
            'category': forms.Select(attrs={'class': "form-control"}),
        }
