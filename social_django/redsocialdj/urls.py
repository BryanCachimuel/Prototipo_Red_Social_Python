from django import views
from django.urls import path
# el . significa que de este mismo directorio se esta haciendo referencia a un archivo (en este caso el archivo views.py)
from . import views

"""
video 4.3 -> se agregan estas librerias  para que se puedan usar archivos estaticos
             + static ->esta parte también sirve para el control de los archivos 

video 5.2 -> se crea la vista el registro de usuarios
"""
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)