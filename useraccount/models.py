from django.db import models
from django.db import models


class User(models.Model):
    profile = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField()
    name = models.CharField(max_length=60)
    caption = models.TextField(max_length=200)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.name

