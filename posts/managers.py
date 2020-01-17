from django.db import models
from django.contrib.auth.models import User


class PostManger(models.Manager):
    def get_aman_posts(self):
        user = User.objects.all()[1]
        return super(PostManger, self).filter(user=user)

    def get_shubham_posts(self):
        user = User.objects.all()[0]
        return super(PostManger, self).filter(user=user)
