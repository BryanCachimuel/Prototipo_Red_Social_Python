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

    # función para saber los seguidores que tengo
    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
                                .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

    # función para saber cuantas personas me siguen
    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
                                .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)


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


"""
video 10.1 se crea una nueva tabla donde se llevara las relaciones entre usuarios
"""

class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]

