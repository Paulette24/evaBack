from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'templatesAppUno/paises.html')

def chile(request):
    data={
        'titulo':'Chilito',
        'imagen': 'imagenes/chile.jpg'
    }
    return render(request, 'templatesAppUno/paises.html', data)

def argentina(request):
    data={
        'titulo':'Argentina',
        'imagen': 'imagenes/argentina.jpg'
    }
    return render(request, 'templatesAppUno/paises.html', data)

def brasil(request):
    data={
        'titulo':'Brasil',
        'imagen': 'imagenes/brasil.jpg'
    }
    return render(request, 'templatesAppUno/paises.html', data)