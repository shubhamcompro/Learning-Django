from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
