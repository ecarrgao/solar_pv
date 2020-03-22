from django import forms
from django.contrib.auth.forms import UserCreationForm

from solarpv.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=8, help_text='Required, must be at most 8 characters long.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'prefix', 'firstname', 'middlename', 'lastname', 'job_title', 'email', 'officephone', 'cellphone')
