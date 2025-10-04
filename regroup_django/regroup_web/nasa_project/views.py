from django.shortcuts import render, get_object_or_404
from .models import NASAChallenge, Hito, Innovacion

def index(request):
    """Página principal del proyecto NASA"""
    challenge = NASAChallenge.objects.first()
    hitos = Hito.objects.filter(proyecto=challenge) if challenge else []
    innovaciones = Innovacion.objects.filter(proyecto=challenge)[:3] if challenge else []
    
    context = {
        'challenge': challenge,
        'hitos': hitos,
        'innovaciones': innovaciones,
    }
    return render(request, 'nasa_project/index.html', context)

def challenge_detail(request, pk):
    """Detalle del challenge NASA"""
    challenge = get_object_or_404(NASAChallenge, pk=pk)
    hitos = challenge.hitos.all()
    innovaciones = challenge.innovaciones.all()
    
    context = {
        'challenge': challenge,
        'hitos': hitos,
        'innovaciones': innovaciones,
    }
    return render(request, 'nasa_project/challenge_detail.html', context)

def innovaciones_list(request):
    """Lista de innovaciones tecnológicas"""
    innovaciones = Innovacion.objects.select_related('proyecto').all()
    
    context = {
        'innovaciones': innovaciones,
    }
    return render(request, 'nasa_project/innovaciones_list.html', context)

def timeline(request):
    """Timeline del proyecto"""
    challenge = NASAChallenge.objects.first()
    hitos = Hito.objects.filter(proyecto=challenge).order_by('fecha') if challenge else []
    
    context = {
        'challenge': challenge,
        'hitos': hitos,
    }
    return render(request, 'nasa_project/timeline.html', context)