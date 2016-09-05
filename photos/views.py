from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def hello(request):
    nombre = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    return HttpResponse("Hello {0}, {1}".format(nombre, apellido))