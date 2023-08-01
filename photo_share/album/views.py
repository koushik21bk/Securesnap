from typing import Any, Dict
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import AlbumCreationForm
from .models import Album, AlbumImage
from user.models import User


class AlbumCreationView(CreateView):
    """Use this view to create new photo albums"""
    model = Album
    template_name = 'album/create-album.html'
    form_class = AlbumCreationForm

    def get_success_url(self) -> str:
        return reverse_lazy('user:profile', args=[self.request.user.slug])

    def form_valid(self, form):
        form.instance.user = self.request.user
        images = self.request.FILES.getlist('images')
        for image in images:
            photo = AlbumImage.objects.create(
                name=image.name,
                image=image,
                album=self.get_object,
                user=self.request.user
            )
            photo.save()
        return super().form_valid(form)


class AlbumsView(ListView):
    """Use this view to list all albums of the profile user"""
    model = Album
    template_name = 'album/albums.html'
    context_object_name = 'albums'

    def get_queryset(self):
        user = self.kwargs['slug']
        return Album.objects.filter(user__username=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = User.objects.get(
            username=self.kwargs['slug'])
        return context


class AlbumView(DetailView):
    model = Album
    template_name = 'album/album.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = AlbumImage.objects.filter(
            album__id=self.kwargs['pk'])
        return context
