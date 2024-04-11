from django.urls import path
from .views import daily_quote

urlpatterns = [
    path("today/", daily_quote, name="daily_quote"),
]
