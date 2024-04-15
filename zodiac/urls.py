from django.urls import path
from . import views

app_name = "zodiac"

urlpatterns = [
    path("today/", views.daily_zodiac, name="daily_fortune"),
]
