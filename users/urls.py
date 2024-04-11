# users/urls.py
from django.urls import path
from .views import LoginView, RegisterView

app_name = "users"  # 네임스페이스 설정

urlpatterns = [
    path("", LoginView.as_view(), name="login"),  # 로그인 뷰 연결
    path("signup/", RegisterView.as_view(), name="register"),  # 회원가입 뷰 연결
]
