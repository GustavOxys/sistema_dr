from django.shortcuts import render
from dashboard.models import Atendimento
from dashboard.models import Paciente
from django.http import HttpResponse
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm
import sys
import time

def log(message):
    # Obtém o tempo atual em milissegundos
    current_time = int(time.time() * 1000)

    # Adiciona o tempo à mensagem
    message_with_time = f"{current_time}: {message}"

    # Imprime a mensagem
    print(message_with_time)



def atendimento_form(request, paciente_id):    
    log("LOG dentro da view atendimento_form")   

    paciente = Paciente.objects.get(id=paciente_id)    
    log('LOG variavl "paciente" criada e pegou id')

    form = AtendimentoForm(instance=Atendimento(paciente=paciente))    
    log('LOG variavl "form" criado com instancia atendimento paciente=paciente')


    return render(request, 'prontuarios/form_atendimento.html', {'form': form})







