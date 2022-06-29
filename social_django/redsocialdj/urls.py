from django import views
from django.urls import path
# el . significa que de este mismo directorio se esta haciendo referencia a un archivo (en este caso el archivo views.py)
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
]