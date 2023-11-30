from django.shortcuts import render
from dashboard.models import Atendimento
from dashboard.models import Paciente
from django.http import HttpResponse
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm


def atendimento_form(request, paciente_id):
    print('dentro da view atendimento_form')
    paciente = Paciente.objects.get(id=paciente_id)
    print('var paciente criada e pegou id')

    form = AtendimentoForm(instance=Atendimento(paciente=paciente))
    print('var form criado com instancia atendimento paciente=paciente')


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
