from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Dashboard
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # Patient
    path('patient/create/', views.create, name='create'),
    path('pacientes/', views.pacientes, name='pacientes'),

    # Agenda
    path('agenda/', views.agenda, name='agenda'),

    # Prontuários
    path('prontuarios/', views.prontuarios, name='prontuarios'),

    # Prontuário
    
    path('prontuario/<int:paciente_id>/', views.prontuario, name='prontuario'),
    path('atendimento/<int:paciente_id>/', views.atendimento_form, name='atendimento_form'),

    path('create_test', views.create_test, name='create_test'),
    path('prontuario/atendimento/teste', views.teste, name='teste'),
    
    # Relatórios
    path('relatorios/', views.relatorios, name='relatorios'),

    # Configurações
    path('configuracoes/', views.configuracoes, name='configuracoes'),  


]