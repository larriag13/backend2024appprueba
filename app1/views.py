from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mostrar(request):
    html="hola"
    return HttpResponse("Hola mundo, soy la app pero modificada desde rama 1")
