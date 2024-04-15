from django.db import models


# Create your models here.
class AllZodiac(models.Model):
    date = models.DateField(unique=True)
    all_fortune = models.CharField(max_length=500)


def __str__(self):
    return self.nickname
