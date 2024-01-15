from django.shortcuts import redirect, get_object_or_404, render
from dashboard.models import Paciente, Atendimento
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required(login_url='dashboard:login')
def prontuario(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)

    
    if request.method == 'POST':
        form = AtendimentoForm(paciente_id, request.POST)

        if form.is_valid():
            atendimento = form.save(commit=False)
            atendimento.paciente = paciente
            atendimento.save()
            atendimento.adicionar_atendimento()
            return redirect('dashboard:prontuario', paciente_id=paciente_id)
    else:
        form = AtendimentoForm(paciente_id)

    context = {
        'form': form,
        'paciente': paciente,
        
    }

    return render(request, 'prontuarios/content_prontuario.html', context)
