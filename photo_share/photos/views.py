from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Image
from .forms import ImageUploadForm


class ImageUploadView(CreateView):
    model = Image
    template_name = 'photos/upload.html'
    form_class = ImageUploadForm

    def get_success_url(self) -> str:
        return reverse_lazy('user:profile', args=[self.request.slug])
