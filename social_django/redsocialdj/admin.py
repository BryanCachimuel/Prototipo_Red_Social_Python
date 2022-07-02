from django.contrib import admin
from .models import Post, Profile, Relationship

"""
video 3.2 registrar al usuario creado como superusuario

"""

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)
