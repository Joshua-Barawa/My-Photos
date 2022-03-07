from django.urls import path
from .views import *

urlpatterns = [
    path('login-user/', login_user, name='login-user'),
    path('logout-user/', logout_user, name='logout-user'),
    path('register-user/', register_user, name='register-user'),
]
