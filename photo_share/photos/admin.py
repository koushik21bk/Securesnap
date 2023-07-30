from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
        'status',
        'upload_date',
        'user',
    ]

    list_filter = [
        'upload_date',
        'status',
    ]

    search_fields = [
        'name',
        'user',
    ]

    date_hierarchy = 'upload_date'
