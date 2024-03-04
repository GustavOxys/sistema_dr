from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Atendimento, Agendamento
from django.core.paginator import Paginator


@login_required(login_url='dashboard:login')
def prontuarios(request):
    user = request.user

    prontuarios = Atendimento.objects.filter(paciente__owner=user).order_by('-data_hora_atendimento')
    agendamentos = Agendamento.objects.filter(paciente__owner=user)

    for p in prontuarios:
        print('prontuario:', p.paciente.nome, p.agendamento)

    paginator = Paginator(prontuarios, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'prontuarios' : prontuarios,
        'agendamentos' : agendamentos,
    }

    return render(request, 'prontuarios/prontuarios.html', context)