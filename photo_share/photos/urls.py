from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('photos/upload/', views.ImageUploadView.as_view(), name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
