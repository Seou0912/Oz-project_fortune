from django.urls import path
from . import views
from .views import constellation_fortune

urlpatterns = [
    path("today/", constellation_fortune),
]
