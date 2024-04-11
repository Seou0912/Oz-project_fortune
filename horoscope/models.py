from django.db import models


class UserBirthday(models.Model):
    birthday = models.DateField()
    zodiac_sign = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.zodiac_sign} ({self.birthday})"
