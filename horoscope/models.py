from django.db import models


class UserBirthday(models.Model):
    birth_date = models.DateField()
    zodiac_sign = models.CharField(max_length=10)
    horoscope = models.CharField(max_length=500)

    def __str__(self):
        return self.zodiac_sign
