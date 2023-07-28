from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django import forms
from .models import User
from utils.forms.widgets import text_input, email_input, password_input


class RegistrationForm(forms.ModelForm):
    def clean_password(self) -> str:
        """Hash the password on user creation"""
        password = self.cleaned_data['password']
        password = make_password(password)

        return password

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        widgets = {
            'first_name': text_input,
            'last_name': text_input,
            'username': text_input,
            'email': email_input,
            'password': password_input
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=text_input)
    password = forms.CharField(max_length=150, widget=password_input)
