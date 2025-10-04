from django.contrib import admin
from .models import NASAChallenge, Hito, Innovacion

@admin.register(NASAChallenge)
class NASAChallengeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'año', 'estado']
    list_filter = ['año', 'estado']
    search_fields = ['titulo', 'descripcion_completa']

@admin.register(Hito)
class HitoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'proyecto', 'fecha', 'completado', 'orden']
    list_filter = ['completado', 'proyecto']
    ordering = ['orden', 'fecha']

@admin.register(Innovacion)
class InnovacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tecnologia', 'proyecto']
    list_filter = ['tecnologia', 'proyecto']
    search_fields = ['titulo', 'descripcion']