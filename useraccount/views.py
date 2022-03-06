from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/members/login-user')
def home(request):
    posts = Image.objects.all()
    return render(request, 'useraccount/index.html', {'posts': posts})


@login_required(login_url='/members/login-user')
def get_image_by_id(request, id):
    image = Image.objects.get(pk=id)
    return render(request, "useraccount/post.html", {"image": image})

