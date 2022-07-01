from django.apps import AppConfig

"""
video 7.1 -> se agrega la función ready para que se utilicen las señales
de crear un perfil cada vez que se cree un usuario
"""

class RedsocialdjConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'redsocialdj'

    def ready(self):
        import redsocialdj.signals
        
