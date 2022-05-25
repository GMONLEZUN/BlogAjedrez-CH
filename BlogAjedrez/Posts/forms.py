from cProfile import label
from django import forms

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
    




