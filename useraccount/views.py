from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,  login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


@login_required(login_url='/login-user')
def home(request):
    posts = Image.objects.all()
    follows = Profile.objects.all()[:4]
    return render(request, 'useraccount/index.html', {'posts': posts, "follows": follows})


@login_required(login_url='/login-user')
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


@login_required(login_url='/login-user')
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


@login_required(login_url='/login-user')
def update_post(request, id):
    image = Image.objects.get(id=id)
    form = ImageForm(request.POST or None, instance=image)
    if form.is_valid():
        form.save()
        return redirect("user_profile")
    return render(request, "useraccount/add_post.html", {"form": form})


@login_required(login_url='/login-user')
def delete_post(request, id):
    Image.objects.filter(id=id).delete()
    return redirect('user_profile')


@login_required(login_url='/login-user')
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


@login_required(login_url='/login-user')
def delete_profile(request):
    User.objects.filter(id=request.user.id).delete()
    return logout_user(request)


@login_required(login_url='/login-user')
def like_post(request, id):
    image = Image.objects.get(id=id)
    image.like = image.like + 1
    Image.objects.filter(id=id).update(like=image.like)
    return home(request)


@login_required(login_url='/login-user')
def search_user(request):
    if request.method == "POST":
        search = request.POST["search"]
        users = Image.objects.filter(category=search)
        return render(request, "useraccount/index.html", {"search": search, "users": users})
    return render(request, "useraccount/index.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.success(request, "Invalid username or password")
            return render(request, '/login.html', {})
    else:
        return render(request, 'useraccount/login.html', {})

    return render(request, '/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "successfully logged out")
    return redirect('login-user')


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Registration successful")
            return render(request, 'useraccount/register.html')
    else:
        form = RegistrationForm()
        profile_form = UserProfileForm()
        return render(request, 'useraccount/register.html', {'form': form, 'profile_form': profile_form})

    return render(request, 'useraccount/register.html', {'form': form, 'profile_form': profile_form})