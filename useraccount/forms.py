from django import forms
from .models import Image, Comments


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'name', 'caption')

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['caption'].widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('desc',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs['class'] = 'form-control'

