from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm, UserRegisterForm
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

# video 5.1 -> invocación a la vista para el registro de usuarios
# video 5.4 -> form.save() para guardar los datos dentro de la base de datos
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado satisfactoriamente')
            return redirect('feed')
    else:
        form = UserRegisterForm()
    
    context = {'form':form}
    return render(request, 'social/register.html', context)

"""
8.3 creación de la vista para los post
(User, pk=request.user.pk) -> se obtiene el usario que esta logeado
"""

def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html', {'form' : form})

def profile(request):
    return render(request, 'social/profile.html')
