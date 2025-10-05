from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
import matplotlib.pyplot as plt
import os
import random

def index(request):
    if request.method == 'POST':
        idea = request.POST.get('idea')
        if idea:
            messages.success(request, "¡Gracias por tu propuesta creativa!")
            try:
                generar_grafico_interno()
            except Exception as e:
                print("Error al generar gráfico desde formulario:", e)
        return redirect('residuos_no_reciclables:index')
    return render(request, 'residuos_no_reciclables/index.html')

def generar_grafico(request):
    try:
        generar_grafico_interno()
        return JsonResponse({'status': 'ok'})
    except Exception as e:
        print("Error al generar gráfico desde AJAX:", e)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def generar_grafico_interno():
    estrategias = ['Compactación', 'Incineración', 'Energía', 'Reutilización']
    valores = [random.randint(10, 100) for _ in estrategias]
    colores = ['#0d6efd', '#dc3545', '#ffc107', '#198754']

    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.pie(valores, labels=estrategias, autopct='%1.1f%%', startangle=90, colors=colores)
    ax.set_title('Distribución de Estrategias de Tratamiento de Residuos No Reciclables')
    ax.axis('equal')

    # Ruta absoluta usando BASE_DIR
    output_path = os.path.join(
        settings.BASE_DIR,
        'residuos_no_reciclables', 'static', 'residuos_no_reciclables', 'img',
        'distribucion_residuos_no_reciclables.png'
    )

    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Guardar gráfico
    plt.savefig(output_path)
    plt.close()
