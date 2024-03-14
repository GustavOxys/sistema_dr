from django.shortcuts import render, redirect, get_object_or_404, reverse
from dashboard.forms.agenda.form_agendamento import AgendamentoForm
from dashboard.forms.agenda.form_agendamento_p import AgendamentoFormP
from django.contrib.auth.decorators import login_required
from dashboard.models import Paciente
from django.http import HttpResponse


@login_required(login_url='dashboard:login')
def agendar(request, paciente_id=None):
    form_action = reverse('dashboard:agendar')
    form = AgendamentoForm(user=request.user)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, user=request.user)
        context = {
            'form' : form,
            'form_action' : form_action
        }
        if form.is_valid():
            agendamento = form.save(commit=False)
            if paciente_id:
                paciente = Paciente.objects.get(pk=paciente_id)
                agendamento.paciente = paciente
            agendamento.save()
            return redirect('dashboard:index')
    
    context = {
        'form': form,
        'form_action' : form_action
    }

    return render(request, 'agenda/agendar.html', context)

@login_required(login_url='dashboard:login')
def agendar_paciente(request, paciente_id):
    user = request.user
    paciente = get_object_or_404(Paciente, pk=paciente_id)  # Obtenha o paciente com o ID fornecido

    if request.method == 'POST':
        form = AgendamentoFormP(paciente_id, user, request.POST)  # Passe os dados POST para o formulário

        if form.is_valid():            
            agendamento = form.save(commit=False)
            agendamento.paciente = paciente  # Atribua o paciente ao agendamento            
            agendamento.save()
            
            return redirect('dashboard:index')
        else:
            return HttpResponse("Esta é uma resposta HTTP!")
    else:
        form = AgendamentoFormP(paciente_id=paciente_id, user=user)  # Crie uma instância do formulário sem dados POST

    context = {
        'form': form,
        'paciente': paciente,
    }

    return render(request, 'agenda/agendar_paciente.html', context)
