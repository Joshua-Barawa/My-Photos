from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'name', 'caption')

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['caption'].widget.attrs['class'] = 'form-control'
