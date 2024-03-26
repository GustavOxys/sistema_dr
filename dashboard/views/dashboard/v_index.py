from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from dashboard.models import Agendamento, Atendimento

@login_required(login_url='dashboard:login')
def index(request):
    return _handle_search(request, is_search=False)

@login_required(login_url='dashboard:login')
def search(request):
    return _handle_search(request, is_search=True)

def _handle_search(request, is_search=False):
    search_action = reverse('dashboard:search')
    placeholder_action = 'Buscar um Agendamento'
    id_action = 'query_index'
    name_action = 'q_index'
    data_hora_atual = timezone.now() - timedelta(hours=3)
    data_atual = timezone.localdate()
    mes_atual = timezone.localdate().month

    atendimentos = Atendimento.objects.filter(paciente__owner=request.user)
    atendimentos_diarios = atendimentos.filter(data_atendimento=data_atual)
    atendimentos_mensais = atendimentos.filter(data_atendimento__month=mes_atual)

    valor_mensal = sum(valor.valor_total_mensal for valor in atendimentos_mensais)
    total_mensal = sum(atendimento.total_mensal for atendimento in atendimentos_mensais)
    total_diario = sum(atendimento.total_diario for atendimento in atendimentos_diarios)

    agendamentos_diarios = Agendamento.objects.filter(paciente__owner=request.user, data_agendamento=data_atual)
    agendamento_diario = sum(agendamento.total_diario for agendamento in agendamentos_diarios)

    if is_search:
        search_value = request.GET.get('q_index', '').strip()

        if not search_value:
            return redirect('dashboard:index')

        agendamentos = Agendamento.objects.filter(
            paciente__show=True,
            data_consulta__gt=data_hora_atual,
            paciente__owner=request.user,
            atendido=False
        ).filter(
            Q(paciente__nome__icontains=search_value) |
            Q(convenio__nome__icontains=search_value) |
            Q(procedimento__nome__icontains=search_value)
        ).order_by('data_consulta', 'hora_consulta')

        site_title = 'Search - '
    else:
        agendamentos = Agendamento.objects.filter(
            paciente__owner=request.user,
            paciente__show=True,
            data_consulta__gt=data_hora_atual,
            atendido=False
        ).order_by('data_consulta', 'hora_consulta')

        site_title = ''

    paginator = Paginator(agendamentos, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'agendamentos': agendamentos,
        'atendimentos': atendimentos,
        'total_diario': total_diario,
        'total_mensal': total_mensal,
        'valor_mensal': valor_mensal,
        'agendamento_diario': agendamento_diario,
        'search_action': search_action,
        'placeholder_action': placeholder_action,
        'id_action': id_action,
        'name_action': name_action,
        'site_title': site_title,
    }

    if is_search:
        context['search_value'] = search_value

    return render(request, 'dashboard/index.html', context)
