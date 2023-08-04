from django.contrib import admin
from .models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "slug",
    ]

    search_fields = [
        "username",
        "email",
    ]
