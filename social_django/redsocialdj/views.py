from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import PostForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
@login_required
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


"""
video 9.1 modificamos la función para que podamos ingresar al perfil de
          cada usuario
"""
def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'social/profile.html', {'user':user, 'posts':posts})

# video 10.2 creando el procedimientos de las vistas para los followers y following
def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('feed')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('feed')
