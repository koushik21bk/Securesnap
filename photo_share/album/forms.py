from django import forms
from .models import Album, AlbumImage
from utils.forms.widgets import text_input, select_input, image_input


class AlbumCreationForm(forms.ModelForm):
    """Use this form to create new photo albums"""
    class Meta:
        model = Album

        fields = [
            'name',
            'status',
        ]

        widgets = {
            'name': text_input,
            'status': select_input,
        }


class AlbumImageUploadForm(forms.ModelForm):
    """This form is used to upload images to a photo album"""
    class Meta:
        model = AlbumImage

        fields = [
            'name',
            'image',
        ]

        widgets = {
            'name': text_input,
            'image': image_input,
        }
