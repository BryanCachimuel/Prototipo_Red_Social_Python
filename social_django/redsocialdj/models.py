from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

"""
 video 3.1 Crear los modelos
 linea 21: cascade significa que se eliminará el usuario de la tabla 
           usuario se va a borrar por defecto el perfil o alguna otra 
           referencia que este adjunta al usuario
 
 linea 29: el related_name='posts'-> permitira acceder de manara mas fácil
           a los posts de los usaurios 

video 4.1 linea 22 ->  Se realizará la parte de imagenes de los usuarios

"""

# atributo que va a tener la tabla profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='batman.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'

# atributos que va a tener la tabla post
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    # muestra los post en forma descendente
    class Meta:
        ordering = ['-timestamp']
    
    # muestra la información del post tanto como usuaio como contenido del post
    def __str__(self):
        return f'{self.user.username}: {self.content}'

