from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user.urls")),
    path("", include("photos.urls")),
    path("", include("album.urls")),
    path("api/", include("api.urls")),
    path('new-uploads/', TemplateView.as_view(template_name='new-uploads.html'), name='new-uploads')

]
