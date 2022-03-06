from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/members/login-user')
def home(request):
    posts = Image.objects.all()
    follows = Profile.objects.all()[:4]
    return render(request, 'useraccount/index.html', {'posts': posts, "follows": follows})


@login_required(login_url='/members/login-user')
def get_image_by_id(request, id):
    image = Image.objects.get(pk=id)
    return render(request, "useraccount/post.html", {"image": image})


@login_required(login_url='/members/login-user')
def save_image(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.filter(user=user).get()

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.user = profile
            image.save()
        return redirect("home-page")
    else:
        form = ImageForm()
    return render(request, "useraccount/add_post.html", {'form': form})
