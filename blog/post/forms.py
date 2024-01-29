from django import forms
from .models import Post

INPUT_CLASS = 'form-control'

class newPostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('category', 'title', 'description', 'image')

    widgets = {
      'category': forms.Select(attrs={
        'class': INPUT_CLASS
      }),
      'title': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'description': forms.Textarea(attrs={
        'class': INPUT_CLASS
      }),
      'image': forms.FileInput(attrs={
        'class': INPUT_CLASS
      })
    }

class editPostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('category', 'title', 'description', 'image')

    widgets = {
      'category': forms.Select(attrs={
        'class': INPUT_CLASS
      }),
      'title': forms.TextInput(attrs={
        'class': INPUT_CLASS
      }),
      'description': forms.Textarea(attrs={
        'class': INPUT_CLASS
      }),
      'image': forms.FileInput(attrs={
        'class': INPUT_CLASS
      })
    }