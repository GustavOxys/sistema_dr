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

    # Agenda/CRUD    
    path('agendar/', views.agendar, name='agendar'), 
    path('agendar/<int:paciente_id>/', views.agendar_paciente, name='agendar_paciente'), 
    path('agendamento/<int:agendamento_id>/', views.read_agendamento, name='read_agendamento'), 
    path('agendamento/<int:agendamento_id>/update/',views.update_agendamento, name='update_agendamento'), 
    path('agendamento/<int:agendamento_id>/delete/',views.delete_agendamento, name='delete_agendamento'), 
    
    # Pacientes/CRUD/Search    
    path('pacientes/', views.pacientes, name='pacientes'),
    path('patient/create/', views.create, name='create'),
    path('patient/<int:paciente_id>/', views.read_patient, name='read_patient'),    
    path('patient/<int:paciente_id>/update/', views.update_patient, name='update_patient'),    
    path('patient/<int:paciente_id>/delete/', views.delete_patient, name='delete_patient'), 
    path('search_patient/', views.search_patient, name='search_patient'),

    # Prontuários
    path('prontuarios/', views.prontuarios, name='prontuarios'),

    # Atendimento
    
    path('atendimento/<int:agendamento_id>/', views.atendimento, name='atendimento'),
    path('atendimento/<int:paciente_id>/', views.atendimento_form, name='atendimento_form'),

    
    
    # Relatórios
    path('relatorios/', views.relatorios, name='relatorios'),

    # Configurações
    path('configuracoes/', views.configuracoes, name='configuracoes'),  


]