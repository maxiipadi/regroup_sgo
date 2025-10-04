from django.urls import path
from . import views

app_name = 'puntos_reciclaje'

urlpatterns = [
    path('', views.index, name='index'),
    path('mapa/', views.mapa, name='mapa'),
    path('punto/<int:pk>/', views.punto_detail, name='punto_detail'),
    path('solicitar-recoleccion/', views.solicitar_recoleccion, name='solicitar_recoleccion'),
]