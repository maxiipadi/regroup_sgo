from django.contrib import admin
from .models import CategoriaRAEE, MaterialRecuperable, InfoRAEE

@admin.register(CategoriaRAEE)
class CategoriaRAEEAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'color']
    search_fields = ['nombre']

@admin.register(MaterialRecuperable)
class MaterialRecuperableAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'simbolo_quimico', 'porcentaje_recuperacion', 'valor_mercado', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nombre', 'simbolo_quimico']

@admin.register(InfoRAEE)
class InfoRAEEAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'fecha_publicacion']
    list_filter = ['categoria', 'fecha_publicacion']
    search_fields = ['titulo', 'contenido']