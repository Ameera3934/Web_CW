from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import DateField, ImageField, DateInput, ClearableFileInput, EmailField, EmailInput

from .models import User
from django import forms

class RegisterForm(UserCreationForm):
    dob = DateField(label="dob")
    profile_image = ImageField(label="Profile Image")

    class Meta:
        fields = UserCreationForm.Meta.fields + ('dob', 'profile_image')
        model = User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)