from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Image
from .forms import ImageUploadForm


class IndexView(ListView):
    model = Image
    template_name = "index.html"
    context_object_name = "images"

    def get_queryset(self):
        """Display `public` photos only"""
        return Image.objects.filter(status=Image.Status.PUBLIC)


class ImageUploadView(CreateView):
    """Use this view to upload images"""

    model = Image
    template_name = "photos/upload.html"
    form_class = ImageUploadForm

    def get_success_url(self) -> str:
        return reverse_lazy("user:profile", args=[self.request.user.slug])

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ImageView(DetailView):
    """Use this view to display a image object"""

    model = Image
    template_name = "photos/image.html"
    context_object_name = "image"


class DeleteImageView(DeleteView):
    """Use this view to delete images"""

    model = Image
    template_name = "photos/delete-image.html"
    context_object_name = "image"

    def get_success_url(self) -> str:
        return reverse_lazy("user:profile", args=[self.request.user.slug])
