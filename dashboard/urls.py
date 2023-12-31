from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [

    path('teste', views.teste, name='teste'),
    # Users
    path('user/create/', views.register_user, name='register_user'),

    # Dashboard
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # Patient/CRUD
    path('pacientes/', views.pacientes, name='pacientes'),      
    path('patient/create/', views.create, name='create'),
    

    # Agenda
    path('agenda/', views.agenda, name='agenda'),

    # Prontuários
    path('prontuarios/', views.prontuarios, name='prontuarios'),

    # Prontuário
    
    path('prontuario/<int:paciente_id>/', views.prontuario, name='prontuario'),
    path('atendimento/<int:paciente_id>/', views.atendimento_form, name='atendimento_form'),

    
    
    # Relatórios
    path('relatorios/', views.relatorios, name='relatorios'),

    # Configurações
    path('configuracoes/', views.configuracoes, name='configuracoes'),  


]