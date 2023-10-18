from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from dashboard.models import Paciente
from django.utils import timezone
from django.core.paginator import Paginator

#o Q é uma função para poder utilizar o '|' que faz a função de 'or' e não 'and' na consulta sql

app_name = 'index'


def index(request):
    data_hora_atual = timezone.now()

    pacientes = Paciente.objects\
        .filter(show=True)\
        .filter(data_consulta__gte=data_hora_atual)\
        .order_by('data_consulta', 'hora_consulta')
    
    paginator = Paginator(pacientes, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
    }

    return render(request, 'index.html', context)


def search(request):

    search_value = request.GET.get('q', '').strip()
    data_hora_atual = timezone.now()

    if search_value == '':
        return redirect('dashboard:index')    

    pacientes = Paciente.objects\
        .filter(show=True)\
        .filter(data_consulta__gte=data_hora_atual)\
        .filter(
            Q(nome__icontains=search_value)|
            Q(convenio__nome__icontains=search_value)|             
            Q(procedimento__nome__icontains=search_value)
            )\
        .order_by('data_consulta', 'hora_consulta')
    
    paginator = Paginator(pacientes, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'site_title' : 'Search - ',
        'search_value' : search_value,
    }

    return render(request, 'index.html', context)