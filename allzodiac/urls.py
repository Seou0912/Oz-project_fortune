from django.urls import path
from allzodiac.views import daily_allzodiac

app_name = "all"
urlpatterns = [
    path("today/all/", daily_allzodiac, name="allzodic"),
]
