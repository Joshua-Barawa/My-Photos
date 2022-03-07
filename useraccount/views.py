from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from members.views import logout_user


@login_required(login_url='/members/login-user')
def home(request):
    posts = Image.objects.all()
    follows = Profile.objects.all()[:4]
    return render(request, 'useraccount/index.html', {'posts': posts, "follows": follows})


@login_required(login_url='/members/login-user')
def get_image_by_id(request, id):
    image = Image.objects.get(pk=id)

    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.filter(user=user).get()
    try:
        comments = Comments.objects.filter(post_id=id)
    except Comments.DoesNotExist:
        comments = None

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = image
            comment.name = profile
            comment.save()
            image = Image.objects.get(id=id)
            image.comment = image.comment + 1

            Image.objects.filter(id=id).update(comment=image.comment)
        return redirect("home-page")
    else:
        form = CommentForm()
    return render(request, "useraccount/post.html", {"image": image, "comments": comments, "form": form})


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


@login_required(login_url='/members/login-user')
def user_profile(request):
    user = User.objects.get(id=request.user.id)
    form = UpdateForm(request.POST or None, instance=user.profile)
    try:
        posts = Image.objects.filter(user=user.profile)
    except Image.DoesNotExist:
        posts = None
    if form.is_valid():
        form.save()
        return redirect("user_profile")
    return render(request, "useraccount/profile.html", {"user": user, "posts": posts, "form": form})


def delete_profile(request):
    User.objects.filter(id=request.user.id).delete()
    return logout_user(request)

