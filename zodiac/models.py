from django.db import models


class Zodiac(models.Model):
    nickname = models.CharField(max_length=100)
    today_fortune = models.TextField()

    def __str__(self):
        return self.name
