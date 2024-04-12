from django.urls import path
from .views import login_view, logout_view, signup

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup, name="signup"),
]
