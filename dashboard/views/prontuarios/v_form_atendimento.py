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


def teste(request):
    return render(request, 'prontuarios/teste-form.html')




def create_test(request):
    
    if request.method == 'POST':
        altura = request.POST['altura']
        peso = request.POST['peso']        
        paciente_id = request.POST['paciente_id']  # Obtenha o paciente_id do formulário

        try:
            paciente = Paciente.objects.get(pk=paciente_id)
        except Paciente.DoesNotExist:
            return HttpResponse('Paciente não encontrado')

        novo_atendimento = Atendimento(altura=altura, peso=peso, paciente=paciente)
        

        try:
            novo_atendimento.full_clean()
            novo_atendimento.save()
            
            success = 'Profile created successfully for ' + paciente.nome
            
            return HttpResponse(success)
        except Exception as e:
            print(f'Erro ao salvar o atendimento: {e}')
            return HttpResponse('Houve um erro ao salvar o atendimento')
    else:
        return HttpResponse('Método não permitido')
