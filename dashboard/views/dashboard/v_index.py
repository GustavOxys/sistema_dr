from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from dashboard.models import Paciente
from django.utils import timezone
from datetime import timedelta, datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from dashboard.models import Atendimento


#o Q é uma função para poder utilizar o '|' que faz a função de 'or' e não 'and' na consulta sql

app_name = 'index'


def index(request):
    atendimentos = Atendimento.objects.all()
    data_hora_atual =  timezone.now() - timedelta(hours=3)
    hoje = datetime.now()

    atendimentos_do_dia = Atendimento.objects.filter(
        data_atendimento__year=hoje.year,
        data_atendimento__month=hoje.month,
        data_atendimento__day=hoje.day
    )

    total_diario = atendimentos_do_dia.count()
    

    pacientes = Paciente.objects\
        .filter(owner=request.user, show=True)\
        .filter(Q(data_consulta__gt=data_hora_atual) | (Q(data_consulta=data_hora_atual, hora_consulta__gte=data_hora_atual)))\
        .order_by('data_consulta', 'hora_consulta')
        
    
    paginator = Paginator(pacientes, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    status_css_mapping = {
        'Pendente': 'pendente',
        'Cancelado': 'cancelado',
        'Confirmado': 'confirmado',
        # Outros mapeamentos aqui
        }

    context = {
        'page_obj' : page_obj,
        'status_css_mapping': status_css_mapping,
        'total_diario' : total_diario,
    }

    return render(request, 'dashboard/index.html', context)

@login_required(login_url='dashboard:login')
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

    return render(request, 'dashboard/index.html', context)