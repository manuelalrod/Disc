from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def detalle(request):
    return render(request, 'detalle.html')


def funcion(request):
    return render(request, 'funcion.html')