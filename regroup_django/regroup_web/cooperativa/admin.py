from django.contrib import admin
from .models import Miembro, Proyecto, ImpactoAmbiental

@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'rol', 'especialidad', 'fecha_ingreso', 'activo']
    list_filter = ['rol', 'activo']
    search_fields = ['usuario__username', 'usuario__first_name', 'usuario__last_name']

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado', 'fecha_inicio', 'presupuesto']
    list_filter = ['estado']
    search_fields = ['nombre', 'descripcion']
    filter_horizontal = ['responsables']

@admin.register(ImpactoAmbiental)
class ImpactoAmbientalAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'toneladas_recicladas', 'co2_evitado', 'empleos_generados', 'dispositivos_procesados']
    list_filter = ['fecha']
    date_hierarchy = 'fecha'