from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from solarpv.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=8, help_text='Required, must be at most 8 characters long.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'prefix', 'firstname', 'middlename', 'lastname', 'job_title', 'email', 'officephone', 'cellphone', 'client')

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
