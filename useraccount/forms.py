from django import forms
from .models import Image, Comments, Profile
from django.contrib.auth.models import User


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


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = form = ('profile_photo', 'bio')

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['profile_photo'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['class'] = 'form-control'
