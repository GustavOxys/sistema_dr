from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [

    path('teste', views.teste, name='teste'),
    # Users
    path('user/create/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login'),
    path('login_or_register/', views.login_or_register, name='login_or_register'),
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

    # Prontuários/CRUD
    path('prontuarios/', views.prontuarios, name='prontuarios'),
    path('prontuarios/<int:paciente_id>/', views.prontuarios_especificos, name='prontuarios_especificos'),
    path('prontuario/<int:prontuario_id>/', views.read_prontuario, name='read_prontuario'),
    path('prontuario/<int:prontuario_id>/update/', views.update_prontuario, name='update_prontuario'),
    #path('prontuarios/<int:prontuario_id>/delete/', views.delete_prontuario,name='delete_prontuario'),    

    # Atendimento    
    path('atendimento/<int:agendamento_id>/', views.atendimento, name='atendimento'),
       
    
    # Configurações
    path('configuracoes/', views.configuracoes, name='configuracoes'),

    # Configurações/Convênios/CRUD

    path('convenios/', views.convenios, name='convenios'),
    path('convenio/create/', views.create_convenio, name='create_convenio'),
    path('convenio/<int:convenio_id>/', views.read_convenio, name='read_convenio'),
    path('convenio/update/<int:convenio_id>/', views.update_convenio, name='update_convenio'),
    path('convenio/delete/<int:convenio_id>/', views.delete_convenio, name='delete_convenio'),



]