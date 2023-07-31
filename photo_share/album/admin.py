from django.contrib import admin
from .models import Album


@admin.register(Album)
class AlbumModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
        'status',
        'upload_date',
        'user',
    ]

    search_fields = [
        'name',
        'user',
    ]

    date_hierarchy = 'upload_date'
