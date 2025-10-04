from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Miembro, Proyecto, ImpactoAmbiental

def index(request):
    """Página principal de la cooperativa"""
    miembros_destacados = Miembro.objects.filter(activo=True, rol='fundador')
    proyectos_activos = Proyecto.objects.filter(estado='ejecucion')
    
    context = {
        'miembros_destacados': miembros_destacados,
        'proyectos_activos': proyectos_activos,
    }
    return render(request, 'cooperativa/index.html', context)

def miembros_list(request):
    """Lista de miembros de la cooperativa"""
    miembros = Miembro.objects.filter(activo=True).select_related('usuario')
    
    context = {
        'miembros': miembros,
    }
    return render(request, 'cooperativa/miembros_list.html', context)

def miembro_detail(request, pk):
    """Detalle de un miembro"""
    miembro = get_object_or_404(Miembro, pk=pk)
    proyectos = miembro.proyectos.all()
    
    context = {
        'miembro': miembro,
        'proyectos': proyectos,
    }
    return render(request, 'cooperativa/miembro_detail.html', context)

def proyectos_list(request):
    """Lista de proyectos"""
    proyectos = Proyecto.objects.all()
    
    context = {
        'proyectos': proyectos,
    }
    return render(request, 'cooperativa/proyectos_list.html', context)

def proyecto_detail(request, pk):
    """Detalle de un proyecto"""
    proyecto = get_object_or_404(Proyecto, pk=pk)
    responsables = proyecto.responsables.all()
    
    context = {
        'proyecto': proyecto,
        'responsables': responsables,
    }
    return render(request, 'cooperativa/proyecto_detail.html', context)

def impacto(request):
    """Página de impacto ambiental"""
    impactos = ImpactoAmbiental.objects.all()[:12]
    
    # Calcular totales
    total_toneladas = sum(i.toneladas_recicladas for i in impactos)
    total_co2 = sum(i.co2_evitado for i in impactos)
    total_dispositivos = sum(i.dispositivos_procesados for i in impactos)
    
    # Calcular equivalencias
    arboles_plantados = int(total_co2 * 50)
    km_no_recorridos = int(total_co2 * 4000)
    hogares_mes = int(total_toneladas * 120)
    
    context = {
        'impactos': impactos,
        'total_toneladas': total_toneladas,
        'total_co2': total_co2,
        'total_dispositivos': total_dispositivos,
        'arboles_plantados': arboles_plantados,
        'km_no_recorridos': km_no_recorridos,
        'hogares_mes': hogares_mes,
    }
    return render(request, 'cooperativa/impacto.html', context)

def unirse(request):
    """Formulario para unirse a la cooperativa"""
    if request.method == 'POST':
        messages.success(request, '¡Gracias por tu interés! Nos pondremos en contacto pronto.')
    
    return render(request, 'cooperativa/unirse.html')