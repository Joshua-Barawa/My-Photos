from django.shortcuts import render


def login_user(request):
    return render(request, 'members/login.html', {})