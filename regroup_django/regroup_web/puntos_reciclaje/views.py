from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import PuntoReciclaje, Recoleccion

def index(request):
    """Página principal de puntos de reciclaje"""
    puntos = PuntoReciclaje.objects.filter(activo=True)
    
    # Filtros por ciudad
    ciudad = request.GET.get('ciudad')
    if ciudad:
        puntos = puntos.filter(ciudad__icontains=ciudad)
    
    context = {
        'puntos': puntos,
    }
    return render(request, 'puntos_reciclaje/index.html', context)

def mapa(request):
    """Mapa interactivo de puntos de reciclaje"""
    puntos = PuntoReciclaje.objects.filter(activo=True)
    
    # Convertir a formato JSON para el mapa
    puntos_json = [
        {
            'id': p.id,
            'nombre': p.nombre,
            'tipo': p.tipo,
            'direccion': p.direccion,
            'lat': float(p.latitud),
            'lng': float(p.longitud),
        }
        for p in puntos
    ]
    
    context = {
        'puntos': puntos,
        'puntos_json': puntos_json,
    }
    return render(request, 'puntos_reciclaje/mapa.html', context)

def punto_detail(request, pk):
    """Detalle de un punto de reciclaje"""
    punto = get_object_or_404(PuntoReciclaje, pk=pk)
    recolecciones = punto.recolecciones.all()[:10]
    
    context = {
        'punto': punto,
        'recolecciones': recolecciones,
    }
    return render(request, 'puntos_reciclaje/punto_detail.html', context)

def solicitar_recoleccion(request):
    """Formulario para solicitar recolección"""
    if request.method == 'POST':
        messages.success(request, '¡Solicitud enviada! Te contactaremos pronto.')
    
    puntos = PuntoReciclaje.objects.filter(activo=True)
    
    context = {
        'puntos': puntos,
    }
    return render(request, 'puntos_reciclaje/solicitar_recoleccion.html', context)