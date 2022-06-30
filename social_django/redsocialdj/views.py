from django.shortcuts import render
from .models import *

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

def profile(request):
    return render(request, 'social/profile.html')
