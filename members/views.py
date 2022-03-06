from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,  login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


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
            return redirect('login-user')
    else:
        return render(request, 'members/login.html', {})

    return render(request, 'members/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "successfully logged out")
    return redirect('login-user')


def register_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request. user)
            messages.success(request, "Registration successful")
            return redirect('home-page')
    else:
        form = UserCreationForm()

    return render(request, 'members/register.html', {'form': form})