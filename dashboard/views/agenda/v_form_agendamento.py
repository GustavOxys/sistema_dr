from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms.agenda.form_agendamento import AgendamentoForm
from django.contrib.auth.decorators import login_required
from dashboard.models import Paciente

@login_required(login_url='dashboard:login')
def agendar(request, paciente_id=None):
    form = AgendamentoForm(user=request.user)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, user=request.user)
        if form.is_valid():
            agendamento = form.save(commit=False)
            if paciente_id:
                paciente = Paciente.objects.get(pk=paciente_id)
                agendamento.paciente = paciente
            agendamento.save()
            return redirect('dashboard:agenda')
    
    context = {
        'form': form,
    }

    return render(request, 'agenda/agendar.html', context)

