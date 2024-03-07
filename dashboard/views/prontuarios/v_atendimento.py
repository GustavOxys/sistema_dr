from django.shortcuts import redirect, get_object_or_404, render, reverse
from dashboard.models import Paciente, Atendimento, Agendamento
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required(login_url='dashboard:login')
def atendimento(request, agendamento_id):
    print('dentro de atendimento')
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)    
    form_action = reverse('dashboard:atendimento', args=[agendamento_id])
    print('dentro de atendimento 2')
    
    if request.method == 'POST':        
        form = AtendimentoForm( request.POST, agendamento_id, user=request.user)
        print('dentro de atendimento 5')
        
        if form.is_valid():
            print('dentro de atendimento 6')
            atendimento = form.save(commit=False)            
            atendimento.paciente = agendamento.paciente 
            atendimento.agendamento = agendamento           
            agendamento.atendido = True                      
            atendimento.save()
            agendamento.save()
             
            return redirect('dashboard:index')
        print('dentro de atendimento 35')

    print('dentro de atendimento 3')
    
    form = AtendimentoForm()
    print('dentro de atendimento 4')

    
            
    context = {
        'form': form,
        'agendamento': agendamento,
        'form_action' : form_action,
    }
    return render(request, 'prontuarios/content_prontuario.html', context)
        

            
            
            
                     

    

    
        


