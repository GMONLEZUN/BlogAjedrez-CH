import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PostBio,PostGames


class PostBioForm(forms.ModelForm):
    
    title = forms.CharField(label='Título',widget=forms.TextInput())
    content = forms.CharField(label='Contenido',widget=forms.Textarea())
    image = forms.ImageField(label='Imágen')
    
    class Meta: 
        model = PostBio
        fields = ['title', 'content', 'image']
    

class PostGamesForm(forms.ModelForm):
    
    title = forms.CharField(label='Título',widget=forms.TextInput())
    content = forms.CharField(label='Contenido',widget=forms.Textarea())
    image = forms.ImageField(label='Imágen')
    
    class Meta: 
        model = PostGames
        fields = ['title', 'content', 'image']
    


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, label="Usuario",widget=forms.TextInput(attrs={'class': 'campo-user'}))
    email = forms.EmailField(required=True, label="Email",widget=forms.EmailInput(attrs={'class': 'campo-email'}))
    password1= forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'campo-password1'}))
    password2= forms.CharField(label="Confirmar password", widget=forms.PasswordInput(attrs={'class': 'campo-password2'}))

    class Meta:
        model = User
        fields=("username", "email", "password1", "password2")
        help_texts = {
            "username": None,
            "email": None,
            "password1": None,
            "password2": None,
        }