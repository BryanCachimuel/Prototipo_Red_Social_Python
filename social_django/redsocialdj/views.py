from django.shortcuts import render

"""
Creación de las vistas para verificar si los templates estan correctamente puestos.
en el return se pone la ruta de los templates a utilizarse
"""
def feed(request):
    return render(request, 'social/feed.html')

def profile(request):
    return render(request, 'social/profile.html')
