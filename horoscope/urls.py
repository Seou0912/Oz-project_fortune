from django.urls import path
from . import views


app_name = "star"

urlpatterns = [
    path("today/", views.fortune, name="fortune"),
]
