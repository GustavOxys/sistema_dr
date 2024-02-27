from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from dashboard.models import Paciente, Agendamento
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



#o Q é uma função para poder utilizar o '|' que faz a função de 'or' e não 'and' na consulta sql

@login_required(login_url='dashboard:login')
def pacientes(request):
    data_hora_atual =  timezone.now() - timedelta(hours=3)
    user = request.user
    pacientes = Paciente.objects.filter(owner=user).order_by('-id')
        
    
    paginator = Paginator(pacientes, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'pacientes': pacientes,
    }

    return render(request, 'pacientes/pacientes.html', context)

@login_required(login_url='dashboard:login')
def search_patient(request):

    search_value_patient = request.GET.get('q_patient', '').strip()
    

    if search_value_patient == '':
        print('dentro de search value patient')
        return redirect('dashboard:pacientes')    

    pacientes = Paciente.objects\
        .filter(show=True)\
        .filter(owner=request.user)\
        .filter(
        Q(telefone__icontains=search_value_patient)|
        Q(nome__icontains=search_value_patient)|            
        Q(id__icontains=search_value_patient)
        )\
        .order_by('id')
    
    paginator = Paginator(pacientes, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'site_title' : 'Search - ',
        'search_value_patient' : search_value_patient
        ,
        'pacientes': pacientes,
    }

    return render(request, 'pacientes/pacientes.html', context)