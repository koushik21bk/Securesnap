from django import forms
from .models import Album
from utils.forms.widgets import text_input, select_input


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
