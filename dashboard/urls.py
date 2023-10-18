from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('agenda/', views.agenda, name='agenda'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('prontuarios/', views.prontuarios, name='prontuarios'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),

]