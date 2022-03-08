from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_photo = CloudinaryField()
    bio = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Image(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    image = CloudinaryField()
    name = models.CharField(max_length=60)
    caption = models.TextField(max_length=200)
    like = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comments(models.Model):
    post_id = models.ForeignKey(Image, on_delete=models.CASCADE, blank=False, null=False)
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.post_id.name

