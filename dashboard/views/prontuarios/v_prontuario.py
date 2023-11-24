from django.shortcuts import render, get_object_or_404
from dashboard.models import Paciente

def prontuario(request, paciente_id):

    paciente = get_object_or_404(Paciente, pk=paciente_id)
    context = {
        'paciente' : paciente
    }
    print('dentro da view prontuario')

    return render(request, 'prontuarios/_content_prontuario.html', context)