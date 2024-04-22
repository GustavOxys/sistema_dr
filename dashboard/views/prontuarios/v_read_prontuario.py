from django.shortcuts import render, get_object_or_404
from dashboard.models import Atendimento
from django.contrib.auth.decorators import login_required


@login_required(login_url='dashboard:login_or_register')
def read_prontuario(request, prontuario_id):
    prontuario = get_object_or_404(Atendimento, pk=prontuario_id)
    return render(request, 'prontuarios/read_prontuario.html', {'prontuario' : prontuario})