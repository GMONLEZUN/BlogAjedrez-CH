from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, label="Usuario",widget=forms.TextInput(attrs={'class': 'campo-user', 'placeholder':'Nombre de usuario'}))
    email = forms.EmailField(required=True, label="Email",widget=forms.EmailInput(attrs={'class': 'campo-email', 'placeholder':'Correo electrónico'}))
    password1= forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'campo-password1', 'placeholder':'Contraseña'}))
    password2= forms.CharField(label="Confirmar password", widget=forms.PasswordInput(attrs={'class': 'campo-password2', 'placeholder':'Confirmar contraseña'}))

    class Meta:
        model = User
        fields=("username", "email", "password1", "password2")
        help_texts = {
            "username": None,
            "email": None,
            "password1": None,
            "password2": None,
        }

class UserLoginForm(AuthenticationForm):    
    username = forms.CharField(required=True, label="Usuario",widget=forms.TextInput)
    password = forms.CharField(required=True, label="Contraseña",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=("username", "password")
        help_texts = {
            "username": None,
            "password": None,
        }

class UserEditForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email",widget=forms.EmailInput(attrs={'class': 'campo-email', 'placeholder':'Modificar correo electrónico'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'campo-password1', 'placeholder':'Modificar contraseña'}))
    password2 = forms.CharField(label="Confirmar password", widget=forms.PasswordInput(attrs={'class': 'campo-password2', 'placeholder':'Confirmar contraseña'}))

    last_name: forms.CharField(widget=forms.TextInput(attrs={'class': 'campo-lastname', 'placeholder':'Apellido'}))
    first_name: forms.CharField(widget=forms.TextInput(attrs={'class': 'campo-firstname', 'placeholder':'Nombre'}))

    class Meta:
        model = User
        fields=("email", "password1", "password2","last_name", "first_name")
        help_texts = {
            "email": None,
            "password1": None,
            "password2": None,
        }

class AvatarForm(forms.Form):
    image = forms.ImageField(label="Avatar")