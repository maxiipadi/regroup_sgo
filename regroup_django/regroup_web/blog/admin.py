from django.contrib import admin
from .models import Categoria, Post, Comentario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'fecha_publicacion', 'publicado', 'vistas']
    list_filter = ['publicado', 'categoria', 'fecha_publicacion']
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha_publicacion'

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'post', 'fecha', 'aprobado']
    list_filter = ['aprobado', 'fecha']
    search_fields = ['nombre', 'email', 'contenido']
    actions = ['aprobar_comentarios']
    
    def aprobar_comentarios(self, request, queryset):
        queryset.update(aprobado=True)
    aprobar_comentarios.short_description = "Aprobar comentarios seleccionados"