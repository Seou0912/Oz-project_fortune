from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    nickname = models.CharField(max_length=50)
    mbti = models.CharField(max_length=4)
    quote = models.CharField(max_length=300)


def __str__(self):
    return self.user
