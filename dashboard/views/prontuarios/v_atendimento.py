from django.shortcuts import redirect, get_object_or_404, render
from dashboard.models import Paciente, Atendimento, Agendamento
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required(login_url='dashboard:login')
def atendimento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)    
    
    if request.method == 'POST':        
        form = AtendimentoForm(agendamento_id, request.POST)
        
        if form.is_valid():
            atendimento = form.save(commit=False)            
            atendimento.paciente = agendamento.paciente            
            agendamento.atendido = True                      
            atendimento.save()
            agendamento.save()
             
            return redirect('dashboard:index')
    else:
        form = AtendimentoForm(agendamento_id=agendamento_id)
    
            
    context = {
        'form': form,
        'agendamento': agendamento,
    }
    return render(request, 'prontuarios/content_prontuario.html', context)
        

            
            
            
                     

    

    
        


