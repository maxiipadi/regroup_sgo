from django.urls import path
from . import views

app_name = 'residuos_no_reciclables'

urlpatterns = [
    path('', views.index, name='index'),
    path('generar-grafico/', views.generar_grafico, name='generar_grafico'),
]
