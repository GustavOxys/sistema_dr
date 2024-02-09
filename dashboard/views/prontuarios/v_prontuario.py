from django.shortcuts import redirect, get_object_or_404, render
from dashboard.models import Paciente, Atendimento
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required(login_url='dashboard:login')
def prontuario(request, paciente_id):
    print(' dentro da func pront', paciente_id)
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    print(request.method)

    
    if request.method == 'POST':
        print('se o metodo é post')
        form = AtendimentoForm(paciente_id, request.POST)
        print('se o metodo é post dps do form')


        if form.is_valid():
            print('se o form é valido')
            atendimento = form.save(commit=False)
            atendimento.paciente = paciente
            print('dentro do form is valid, antes do save, total diario:', atendimento.total_diario, 'total mensal', atendimento.total_mensal)
            atendimento.save()  
            print('dentro do form is valid, ', atendimento.total_diario, atendimento.total_mensal)          
            return redirect('dashboard:index')
    else:
        form = AtendimentoForm(paciente_id=paciente_id)

    context = {
        'form': form,
        'paciente': paciente,
        
    }

    return render(request, 'prontuarios/content_prontuario.html', context)
