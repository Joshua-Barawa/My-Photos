from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name='home-page'),
    path('get-image/<int:id>/', get_image_by_id, name="get_image"),
    path('profile/', user_profile, name="user_profile"),

]
