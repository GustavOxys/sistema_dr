from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Agendamento
from django.contrib.auth.decorators import login_required


@login_required(login_url='dashboard:login')
def read_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
    return render(request, 'agenda/read_agendamento.html', {'agendamento' : agendamento})