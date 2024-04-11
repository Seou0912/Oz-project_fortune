from django.urls import path
from . import views

urlpatterns = [
    path("today/", views.Mbti, name="mbti"),
]
