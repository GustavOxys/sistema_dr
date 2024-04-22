from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Agendamento
from dashboard.forms.agenda.form_agendamento import AgendamentoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


@login_required(login_url='dashboard:login_or_register')
def update_agendamento(request, agendamento_id): 
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
    
    form_action = reverse('dashboard:update_agendamento', args=(agendamento_id,))

    if request.method == 'POST':
        
        form = AgendamentoForm(request.POST, instance=agendamento, user=request.user)
        context = {
            'form' : form,
            'form_action': form_action
        }

        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.paciente.owner = request.user
            agendamento.save()
            messages.success(request, 'Agendamento editado com sucesso!')
            return redirect('dashboard:index')
        else:
            messages.error(request, 'Ocorreu algum erro ao salvar o formulário de Agendamento')  
            return render(request, 'agenda/agendar.html', context) 
           
    context = {
        'form' : AgendamentoForm(instance=agendamento, user=request.user),
        'form_action' :form_action
    }

    return render(request, 'agenda/agendar.html', context)
            

            
