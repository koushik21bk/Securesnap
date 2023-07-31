from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('photos/create-album/',
         views.AlbumCreationView.as_view(), name='create-album'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
