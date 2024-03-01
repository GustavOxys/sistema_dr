from django.shortcuts import render, redirect, get_object_or_404, reverse
from dashboard.models import Agendamento
from dashboard.forms.agenda.form_agendamento import AgendamentoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='dashboard:login')
def delete_agendamento(request, agendamento_id): 
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id, )
    print(agendamento)
    agendamento.delete()

    return redirect('dashboard:index')