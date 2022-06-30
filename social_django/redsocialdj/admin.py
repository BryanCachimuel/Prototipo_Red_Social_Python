from django.contrib import admin
from .models import Post, Profile

"""
video 3.2 registrar al usuario creado como superusuario

"""

admin.site.register(Profile)
admin.site.register(Post)
