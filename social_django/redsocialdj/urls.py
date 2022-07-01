from re import template
from django import views
from django.urls import path
# el . significa que de este mismo directorio se esta haciendo referencia a un archivo (en este caso el archivo views.py)
from . import views

"""
video 4.3 -> se agregan estas librerias  para que se puedan usar archivos estaticos
             + static ->esta parte también sirve para el control de los archivos 

video 5.2 -> se crea la vista el registro de usuarios
video 5.5 -> hacemos la invocación en las rutas para las vistas de login y logout

video 8.4 -> creamos la url para la creación del post 
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('post/', views.post, name='post'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)