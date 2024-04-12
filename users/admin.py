from django.contrib import admin
from users.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "nickname",
        "birth_date",
        "mbti",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    filter_horizontal = ()

    list_filter = ("is_active", "is_staff", "is_superuser")
