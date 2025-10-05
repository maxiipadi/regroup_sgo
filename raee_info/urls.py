from django.urls import path
from . import views

app_name = 'raee_info'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('materiales/', views.materiales_list, name='materiales_list'),
]