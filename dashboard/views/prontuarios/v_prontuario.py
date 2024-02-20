from django.shortcuts import redirect, get_object_or_404, render
from dashboard.models import Paciente, Atendimento
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required(login_url='dashboard:login')
def prontuario(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    print('paciente id', paciente.id)
    
    if request.method == 'POST':
        form = AtendimentoForm(paciente_id, request.POST)
        
        if form.is_valid():
            atendimento = form.save(commit=False)
            print('atendimento id', atendimento.id)
            atendimento.paciente = paciente
            print('atendimento id', atendimento.paciente.id)

            
            
            atendimento.save()  
            return redirect('dashboard:index')
    else:
        form = AtendimentoForm(paciente_id=paciente_id)

            
    context = {
        'form': form,
        'paciente': paciente,
    }
    return render(request, 'prontuarios/content_prontuario.html', context)
        

            
            
            
                     

    

    
        


