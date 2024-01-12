from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from dashboard.models import Paciente
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



#o Q é uma função para poder utilizar o '|' que faz a função de 'or' e não 'and' na consulta sql

@login_required(login_url='dashboard:login')
def pacientes(request):
    data_hora_atual =  timezone.now() - timedelta(hours=3)

    pacientes = Paciente.objects.filter(owner=request.user, show=True).order_by('data_consulta', 'hora_consulta')
        
    
    paginator = Paginator(pacientes, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
    }

    return render(request, 'pacientes/pacientes.html', context)

@login_required(login_url='dashboard:login')
def search(request):

    search_value = request.GET.get('q', '').strip()
    

    if search_value == '':
        return redirect('dashboard:pacientes')    

    pacientes = Paciente.objects\
        .filter(show=True)\
            .filter(
            Q(nome__icontains=search_value)|
            Q(convenio__nome__icontains=search_value)|             
            Q(procedimento__nome__icontains=search_value)|
            Q(id__icontains=search_value)
            )\
        .order_by('id')
    
    paginator = Paginator(pacientes, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'site_title' : 'Search - ',
        'search_value' : search_value,
    }

    return render(request, 'pacientes/pacientes.html', context)