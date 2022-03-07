from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name='home-page'),
    path('add-post/', save_image, name="add_post"),
    path('get-image/<int:id>/', get_image_by_id, name="get_image"),
    path('profile/', user_profile, name="user_profile"),
    path('delete-profile/', delete_profile, name="delete_profile"),
    path('like-post/<int:id>', like_post, name="like_post"),
    path('update-post/<int:id>', update_post, name="update_post"),
]
