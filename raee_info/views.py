from django.shortcuts import render, get_object_or_404
from .models import CategoriaRAEE, MaterialRecuperable, InfoRAEE

def index(request):
    """Página principal de información RAEE"""
    categorias = CategoriaRAEE.objects.all()
    info_reciente = InfoRAEE.objects.all()[:6]
    
    context = {
        'categorias': categorias,
        'info_reciente': info_reciente,
    }
    return render(request, 'raee_info/index.html', context)

def categoria_detail(request, pk):
    """Detalle de una categoría RAEE"""
    categoria = get_object_or_404(CategoriaRAEE, pk=pk)
    materiales = categoria.materiales.all()
    informacion = categoria.informacion.all()
    
    context = {
        'categoria': categoria,
        'materiales': materiales,
        'informacion': informacion,
    }
    return render(request, 'raee_info/categoria_detail.html', context)

def materiales_list(request):
    """Lista de materiales recuperables"""
    materiales = MaterialRecuperable.objects.select_related('categoria').all()
    
    context = {
        'materiales': materiales,
    }
    return render(request, 'raee_info/materiales_list.html', context)