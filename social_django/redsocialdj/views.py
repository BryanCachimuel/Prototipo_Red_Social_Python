from email import message
from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm

"""
video 2. Creación de las vistas para verificar si los templates estan correctamente puestos.
         en el return se pone la ruta de los templates a utilizarse

video 3.3 Importamos los modelos de las tablas.
          Dentro de las funciones mandamos a llamar a los modelos
          para que sean visibles en las vistas.

"""
def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'social/feed.html', context)

# video 5.1 -> invocación a la vista para el registro de usuarios
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message.success(request, f'Usuario {username} creado satisfactoriamente')
    else:
        form = UserCreationForm()
    
    context = {'form':form}
    return render(request, 'social/register.html', context)

def profile(request):
    return render(request, 'social/profile.html')
