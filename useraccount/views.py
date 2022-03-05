from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    posts = Image.objects.all()
    return render(request, 'useraccount/index.html', {'posts': posts})
