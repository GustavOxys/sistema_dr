from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [

    path('teste', views.teste, name='teste'),
    # Users
    path('user/create/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login'),
    path('user/logout/', views.logout_user, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
    

    # Dashboard
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # Pacientes
    path('pacientes/', views.pacientes, name='pacientes'),

    # Paciente/CRUD    
    path('patient/create/', views.create, name='create'),
    path('patient/<int:paciente_id>/', views.read_patient, name='read_patient'),    

    # Agenda
    path('agenda/', views.agenda, name='agenda'),
    path('agendar/', views.agendar, name='agendar'), 

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