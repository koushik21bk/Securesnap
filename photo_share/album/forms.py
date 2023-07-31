from django import forms
from .models import Album
from utils.forms.widgets import text_input, image_input, select_input


class AlbumCreationForm(forms.ModelForm):
    """Use this form to create new photo albums"""
    class Meta:
        model = Album

        fields = [
            'name',
            'image',
            'status',
        ]

        widgets = {
            'name': text_input,
            'image': image_input,
            'status': select_input,
        }
