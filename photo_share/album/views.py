from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import AlbumCreationForm
from .models import Album


class AlbumCreationView(CreateView):
    """Use this view to create new photo albums"""
    model = Album
    template_name = 'album/create-album.html'
    form_class = AlbumCreationForm

    def get_success_url(self) -> str:
        return reverse_lazy('user:profile', args=[self.request.user.slug])
