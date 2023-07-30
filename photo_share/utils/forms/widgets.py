"""
This module holds form widgets
"""
from django import forms

# CSS classes for bootstrap input's
attrs = [
    {'class': 'form-control'},
    {'class': 'form-select'},
    {'class': 'form-check-input'},
]

text_input = forms.TextInput(attrs=attrs[0])
email_input = forms.EmailInput(attrs=attrs[0])
password_input = forms.PasswordInput(attrs=attrs[0])
select_input = forms.Select(attrs=attrs[1])
image_input = forms.FileInput(attrs=attrs[0])
