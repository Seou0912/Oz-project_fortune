from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email is required")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Member(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    birth_date = models.DateField()
    nickname = models.CharField(max_length=50)
    mbti = models.CharField(max_length=10)


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", unique=True)
    birth_date = models.DateField(null=True)
    nickname = models.CharField(max_length=10)
    mbti = models.CharField(max_length=10)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email
