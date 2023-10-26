from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'templatesAppUno/index.html')


def electronica(request):
    data={
        'titulo':'Electrónica',
        'producto1':'MAC',
        'producto2':'Celular',
        'producto3':'PlayStation',
        'urls': '/www.inacap.cl',
        'imagen': 'imagenes/producto.jpg'
    }
    return render(request, 'templatesAppUno/productos.html', data)

def juguetes(request):
    data={
        'titulo':'Juguetes',
        'producto1':'Auto',
        'producto2':'Figura de acción',
        'producto3':'Juego de mesa',
        'urls': '/www.inacap.cl',
        'imagen': 'imagenes/producto.jpg'
    }
    return render(request, 'templatesAppUno/productos.html', data)

def ropa(request):
    data={
        'titulo':'Ropa',
        'producto1':'Polera',
        'producto2':'Chaqueta',
        'producto3':'Zapatilla',
        'urls': '/www.inacap.cl',
        'imagen': 'imagenes/producto.jpg'
    }
    return render(request, 'templatesAppUno/productos.html', data)