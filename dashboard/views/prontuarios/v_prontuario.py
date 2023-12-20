from django.shortcuts import redirect, get_object_or_404, render
from dashboard.models import Paciente
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm

def prontuario(request, paciente_id):
    print('dentro da view prontuario')
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    print('depois de capturar o paciente')
    print(request.method)

    if request.method == 'POST':
        print('depois do if method = post')
        print(request.method)


        form = AtendimentoForm(paciente_id, request.POST)

        if form.is_valid():
            atendimento = form.save(commit=False)
            atendimento.paciente = paciente
            atendimento.save()
            return redirect('dashboard:prontuario', paciente_id=paciente_id)
    else:
        form = AtendimentoForm(paciente_id)

    context = {
        'form': form,
        'paciente': paciente
    }

    return render(request, 'prontuarios/content_prontuario.html', context)