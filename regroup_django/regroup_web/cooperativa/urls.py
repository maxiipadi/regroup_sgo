from django.urls import path
from . import views

app_name = 'cooperativa'

urlpatterns = [
    path('', views.index, name='index'),
    path('miembros/', views.miembros_list, name='miembros_list'),
    path('miembro/<int:pk>/', views.miembro_detail, name='miembro_detail'),
    path('proyectos/', views.proyectos_list, name='proyectos_list'),
    path('proyecto/<int:pk>/', views.proyecto_detail, name='proyecto_detail'),
    path('impacto/', views.impacto, name='impacto'),
    path('unirse/', views.unirse, name='unirse'),
]