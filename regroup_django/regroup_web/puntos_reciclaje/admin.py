from django.contrib import admin
from .models import PuntoReciclaje, Recoleccion

@admin.register(PuntoReciclaje)
class PuntoReciclajeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'ciudad', 'provincia', 'activo']
    list_filter = ['tipo', 'ciudad', 'provincia', 'activo']
    search_fields = ['nombre', 'direccion', 'ciudad']

@admin.register(Recoleccion)
class RecoleccionAdmin(admin.ModelAdmin):
    list_display = ['punto', 'fecha', 'cantidad_kg', 'tipo_residuos']
    list_filter = ['fecha', 'punto']
    date_hierarchy = 'fecha'
    search_fields = ['punto__nombre', 'tipo_residuos']