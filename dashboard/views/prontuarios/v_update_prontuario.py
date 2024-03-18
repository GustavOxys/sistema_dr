from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Atendimento
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


@login_required(login_url='dashboard:login')
def update_prontuario(request, prontuario_id): 
    user = request.user
    prontuario = get_object_or_404(Atendimento, pk=prontuario_id)    
    form_action = reverse('dashboard:update_prontuario', args=(prontuario_id,))
    if request.method == 'POST':        
        form = AtendimentoForm(request.POST, instance=prontuario, user=user)
        context = {
            'form' : form,
            'form_action': form_action
        }
        if form.is_valid():            
            prontuario = form.save(commit=False)
            prontuario.agendamento.paciente.owner = user  
            prontuario.editado = True
            prontuario.save()         
            messages.success(request, 'Prontuário editado com sucesso!')            
            return redirect('dashboard:index')
        else:            
            messages.error(request, 'Ocorreu algum erro ao salvar o formulário de Atendimento')  
            return render(request, 'prontuarios/prontuarios.html', context)       
    else:
        form =  AtendimentoForm(instance=prontuario, user=user)     
    context = {
        'form' : form,
        'form_action' :form_action
    }
    return render(request, 'prontuarios/content_prontuario.html', context)
            

            
