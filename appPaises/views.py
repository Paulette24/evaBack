from django.shortcuts import render

# Create your views here.

def chile(request):
    data={
        'titulo':'Chilito',
        'info1':'País largo y angosto que se extiende por el borde occidental de Sudamérica',
        'info2':'Su capital y ciudad más poblada es Santiago.',
        'info3':'Tiene una costa de 6435 km de longitud',
        'info4': 'Moneda: Peso(CLP)',
        'urls': '/www.inacap.cl',
        'imagen': 'imagenes/chile.jpg'
    }
    return render(request, 'templatesAppPaises/index.html', data)

def argentina(request):
    data={
        'titulo':'Argentina',
        'info1':'País de America del Sur, ubicado en el extremo sur y sudeste de dicho subcontinente.',
        'info2':'Su capital: Buenos Aires',
        'info3':'Moneda: Peso(ARS)',
        'info4': 'La economía argentina es la segunda más desarrollada e importante en Sudamérica.',
        'urls': '/www.inacap.cl',
        'imagen': 'imagenes/argentina.jpg'
    }
    return render(request, 'templatesAppPaises/index.html', data)

def brasil(request):
    data={
        'titulo':'Brasil',
        'info1':'Es el tercer país más grande de América, con una superficie estimada en más de 8 500 000 km²,',
        'info2':'Su capital: Brasilia',
        'info3':'Es el séptimo país más poblado del mundo',
        'info4': 'Moneda: Real brasileño(BRL)',
        'urls': '/www.inacap.cl',
        'imagen': 'imagenes/brasil.jpg'
    }
    return render(request, 'templatesAppPaises/index.html', data)