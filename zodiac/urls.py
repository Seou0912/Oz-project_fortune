from django.urls import path
from . import views

urlpatterns = [
    path("today/", views.daily_zodiac, name="daily_zodiac"),
]
