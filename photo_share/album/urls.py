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
    path('photos/<slug:slug>/album/<int:pk>/upload-image/',
         views.AlbumImageUploadView.as_view(), name='upload-image'),
    path('photos/<slug:slug>/album/<int:pk>/delete/',
         views.DeleteAlbumView.as_view(), name='delete-album'),
    path('photos/<slug:slug>/album/<int:album_pk>/image/<int:pk>/delete/',
         views.DeleteAlbumImageView.as_view(), name='delete-album-image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
