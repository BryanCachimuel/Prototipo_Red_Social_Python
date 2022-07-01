from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

"""
video 5.3 se modifica la vista para registrar y se elimina 
          los mensajes de advertencia que se ve en la vista
"""

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:" " for k in fields }

# video 8.1 creación del formulario para crear los posts
class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Qué esta pasando?'}), required=True)

    class Meta:
        model = Post
        fields = ['content']

