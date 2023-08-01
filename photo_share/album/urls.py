from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('photos/<slug:slug>/create-album/',
         views.AlbumCreationView.as_view(), name='create-album'),
    path('photos/<slug:slug>/albums/', views.AlbumsView.as_view(), name='albums'),
    path('photos/<slug:slug>/album/<int:pk>/',
         views.AlbumView.as_view(), name='album'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
