# 프로젝트의 urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),  # 기존 allauth 관련 경로는 유지
    path("", include("users.urls")),  # users 앱의 URL 패턴 포함
    path("dailyquote/", include("dailyquote.urls")),  # dailyquote 앱의 URL 패턴 포함
    path("zodiac/", include("zodiac.urls")),  # zodiac 앱의 URL 패턴 포함
    path("horoscope/", include("horoscope.urls")),  # horoscope 앱의 URL 패턴 포함
    path("mbti/", include("mbti.urls")),  #
    path("allzodiac/", include("allzodiac.urls")),  # allzodiac 앱의 URL 패턴 포함
]
