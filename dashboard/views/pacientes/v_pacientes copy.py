from django.shortcuts import render, redirect, reverse
from django.db.models import Q, Max, OuterRef, Subquery
from dashboard.models import Paciente, Atendimento
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='dashboard:login')
def pacientes(request):
    search_action = reverse('dashboard:search_patient') 
    placeholder_action = 'Buscar um Paciente' 
    id_action = 'query_patient'
    name_action = 'q_patient'
    search_value = request.GET.get('q_patient', '').strip()
    data_hora_atual =  timezone.now() - timedelta(hours=3)
    user = request.user

    pacientes = Paciente.objects\
        .filter(owner=user)\
        .filter(show=True)\
        .order_by('-id')

    ultimos_atendimentos = Atendimento.objects\
        .filter(paciente=OuterRef('pk'))\
        .values('paciente')\
        .annotate(ultimo_atendimento=Max('data_hora_atendimento'))\
        .values('ultimo_atendimento').distinct()    
    

    pacientes_com_atendimentos = pacientes\
        .annotate(ultimo_atendimento=Subquery(ultimos_atendimentos))      
   

    pacientes_com_atendimentos = list(pacientes_com_atendimentos\
        .values('id', 'nome', 'telefone', 'ultimo_atendimento'))     
    
    
    paginator = Paginator(pacientes_com_atendimentos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    for paciente_info in page_obj.object_list:
        if paciente_info['ultimo_atendimento'] is None:
            paciente_info['ultimo_atendimento'] = "Sem atendimentos"

    context = {
        'page_obj': page_obj,
        'search_action': search_action,
        'placeholder_action': placeholder_action,
        'id_action': id_action,
        'name_action': name_action,
    }

    return render(request, 'pacientes/pacientes.html', context)

@login_required(login_url='dashboard:login')
def search_patient(request):
    user = request.user
    search_action = reverse('dashboard:search_patient') 
    placeholder_action = 'Buscar um Paciente' 
    id_action = 'query_patient'
    name_action = 'q_patient'
    search_value = request.GET.get('q_patient', '').strip()
    

    if search_value == '':        
        return redirect('dashboard:pacientes')    

    pacientes = Paciente.objects\
        .filter(show=True)\
        .filter(owner=user)\
        .filter(
        Q(telefone__icontains=search_value)|
        Q(nome__icontains=search_value)|            
        Q(id__icontains=search_value)
        )\
        .order_by('id')

    ultimos_atendimentos = Atendimento.objects\
        .filter(paciente=OuterRef('pk'))\
        .values('paciente')\
        .annotate(ultimo_atendimento=Max('data_hora_atendimento'))\
        .values('ultimo_atendimento').distinct()    
    

    pacientes_com_atendimentos = pacientes\
        .annotate(ultimo_atendimento=Subquery(ultimos_atendimentos))      
   

    pacientes_com_atendimentos = list(pacientes_com_atendimentos\
        .values('id', 'nome', 'telefone', 'ultimo_atendimento'))    
    
    paginator = Paginator(pacientes_com_atendimentos, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    for paciente_info in page_obj.object_list:
        if paciente_info['ultimo_atendimento'] is None:
            paciente_info['ultimo_atendimento'] = "Sem atendimentos"

    context = {
        'page_obj': page_obj,
        'search_action': search_action,
        'placeholder_action': placeholder_action,
        'id_action': id_action,
        'name_action': name_action,
        'site_title': 'Search - ',
        'search_value': search_value,
        'pacientes': pacientes,
    }

    return render(request, 'pacientes/pacientes.html', context)
