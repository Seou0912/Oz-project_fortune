from django.db import models
from users.models import User


class Zodiac(models.Model):
    nickname = models.CharField(max_length=100)
    today_fortune = models.CharField(max_length=500)


def __str__(self):
    return self.nickname
