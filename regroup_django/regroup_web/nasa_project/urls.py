from django.urls import path
from . import views

app_name = 'nasa_project'

urlpatterns = [
    path('', views.index, name='index'),
    path('challenge/<int:pk>/', views.challenge_detail, name='challenge_detail'),
    path('innovaciones/', views.innovaciones_list, name='innovaciones_list'),
    path('timeline/', views.timeline, name='timeline'),
]