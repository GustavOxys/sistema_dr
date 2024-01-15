from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from dashboard.models import Atendimento
from dashboard.models import Paciente
from django.http import HttpResponse
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm
import sys
import time


@login_required(login_url='dashboard:login')
def atendimento_form(request, paciente_id):    
    paciente = Paciente.objects.get(id=paciente_id)      
    form = AtendimentoForm(instance=Atendimento(paciente=paciente))  

    return render(request, 'prontuarios/form_atendimento.html', {'form': form})







