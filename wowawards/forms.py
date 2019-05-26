from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image


class NewPostForm(forms.ModelForm):
    
    class Meta:
        model=Image
        fields=['project_title', 'project_description', 'project_image', 'profile']
        


