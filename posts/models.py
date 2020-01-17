from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .managers import PostManger


class Tag(models.Model):
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'tags'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostManger()

    def __str__(self):
        return self.title

    class Meta:
        default_related_name = 'posts'
