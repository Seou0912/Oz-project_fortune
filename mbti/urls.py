from django.urls import path
from . import views

app_name = "mbti"
urlpatterns = [
    path("today/", views.Mbti, name="Mbti"),
]
