from django.template import Template, Context, loader
from django.http import HttpResponse
from Applic.models import *


def saludar (request,nombre,apellido):
    saludo = f'Hola {nombre} {apellido}'
    return HttpResponse(saludo)

def plant (request):

    
        #templateej = Template(file.read())
        #contextej = Context()
        #vista = templateej.render(contextej)

        patito = 'Cuak'
        plantilla = loader.get_template('bienvenida.html')
        renderr = plantilla.render(patito)

        return HttpResponse(renderr)

