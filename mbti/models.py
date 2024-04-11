from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE)
    mbti = models.CharField(max_length=4)


def __str__(self):
    return self.user.nickname
