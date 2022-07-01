# 7.1 para hacer la creación de perfiles con señales
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver


# video 7.2 ayudara a crear un perfil de un usuario registrado
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

