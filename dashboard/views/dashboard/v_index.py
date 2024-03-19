from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta, datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from dashboard.models import Agendamento, Paciente, Procedimento, Convenio, Atendimento
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


app_name = 'index'


@login_required(login_url='dashboard:login')
def index(request):
    data_hora_atual =  timezone.now() - timedelta(hours=3)    
    data_atual = timezone.localdate() 
    mes_atual = timezone.localdate().month  

    atendimentos = Atendimento.objects.filter(
        paciente__owner=request.user)    

    atendimentos_diarios = Atendimento.objects.filter(
        paciente__owner=request.user, 
        data_atendimento=data_atual,)

    atendimentos_mensais = Atendimento.objects.filter(
        paciente__owner=request.user,
        data_atendimento__month=mes_atual,
    ) 
    valor_mensal = sum(valor.valor_total_mensal for valor in atendimentos_mensais)    
    total_mensal = sum(atendimento.total_mensal for atendimento in atendimentos_mensais)    
    total_diario = sum(atendimento.total_diario for atendimento in atendimentos_diarios)       
    
    agendamentos_diarios = Agendamento.objects.filter(paciente__owner=request.user, data_agendamento=data_atual)     
    agendamento_diario = sum(agendamento.total_diario for agendamento in agendamentos_diarios)
    

    # Realiza consulta SQL e filtra apenas agendamentos do próprio usuário, que seja maior que a data e hora atual e ordena por data e hora do agendamento
    agendamentos = Agendamento.objects\
        .filter(paciente__owner=request.user, paciente__show=True)\
        .filter(Q(data_consulta__gt=data_hora_atual) | (Q(data_consulta=data_hora_atual, hora_consulta__gte=data_hora_atual)))\
        .filter(atendido=False)\
        .order_by('data_consulta', 'hora_consulta')
        
        
    # Lógica da paginação usando Paginator
    paginator = Paginator(agendamentos, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)    

    context = {
        'page_obj' : page_obj,        
        'agendamentos': agendamentos, 
        'atendimentos' : atendimentos,  
        'total_diario' : total_diario,
        'total_mensal': total_mensal,
        'valor_mensal' : valor_mensal,
        'agendamento_diario' : agendamento_diario,           
    }
    return render(request, 'dashboard/index.html', context)



@login_required(login_url='dashboard:login')
def search(request):
    search_value = request.GET.get('q_index', '').strip()
    data_hora_atual =  timezone.now() - timedelta(hours=3) 
    data_atual = timezone.localdate()

    atendimentos = Atendimento.objects.filter(
        paciente__owner=request.user)

    atendimentos_diarios = Atendimento.objects.filter(
        paciente__owner=request.user, 
        data_atendimento=data_atual)

    total_mensal = sum(atendimento.total_mensal for atendimento in atendimentos)    
    total_diario = sum(atendimento.total_diario for atendimento in atendimentos_diarios)       
    
    agendamentos_diarios = Agendamento.objects.filter(paciente__owner=request.user, data_agendamento=data_atual)

    agendamento_diario = sum(agendamento.total_diario for agendamento in agendamentos_diarios)

    if search_value == '':        
        return redirect('dashboard:index')    

    agendamentos = Agendamento.objects\
        .filter(paciente__show=True)\
        .filter(data_consulta__gte=data_hora_atual)\
        .filter(
            Q(paciente__nome__icontains=search_value)|
            Q(convenio__nome__icontains=search_value)|             
            Q(procedimento__nome__icontains=search_value)
            )\
        .filter(paciente__owner=request.user)\
        .order_by('data_consulta', 'hora_consulta')
    
    paginator = Paginator(agendamentos, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'site_title' : 'Search - ',
        'search_value' : search_value,
        'agendamentos': agendamentos, 
        'atendimentos' : atendimentos,  
        'total_diario' : total_diario,
        'total_mensal': total_mensal,
        'agendamento_diario' : agendamento_diario,
    }

    return render(request, 'dashboard/index.html', context)