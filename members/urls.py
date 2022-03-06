
from django.urls import path
from .views import *

urlpatterns = [
    path('login-user/', login_user, name='login-user')

]