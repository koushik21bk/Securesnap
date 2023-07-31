from django.contrib import admin
from .models import Album, AlbumImage


@admin.register(Album)
class AlbumModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
        'creation_date',
        'user',
    ]

    search_fields = [
        'name',
        'user',
    ]

    date_hierarchy = 'creation_date'


@admin.register(AlbumImage)
class AlbumImageModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
        'upload_date',
        'album',
        'user',
    ]

    search_fields = [
        'name',
        'user',
    ]

    date_hierarchy = 'upload_date'
