from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

INPUT_CLASS = 'form-control'


class LoginForm(AuthenticationForm):

  email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Email',
    'class': INPUT_CLASS
  }))

  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Password',
    'class': INPUT_CLASS
  }))

  

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'username','password1', 'password2')
  

  first_name = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'First Name',
    'class': INPUT_CLASS
  }))

  last_name = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Last Name',
    'class': INPUT_CLASS
  }))

  email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Email',
    'class': INPUT_CLASS
  }))

  username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Enter a username',
    'class': INPUT_CLASS
  }))

  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Password',
    'class': INPUT_CLASS
  }))

  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Confirm Password',
    'class': INPUT_CLASS
  }))