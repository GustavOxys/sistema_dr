from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Atendimento
from django import forms
from dashboard.models import Paciente
from django.http import HttpResponse

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = 'queixa_principal', 'historia_molestia_atual', 'historico_e_antecedentes',\
        'exame_fisico', 'altura', 'peso', 'imc', 'diagnostico', 'condutas',

def atendimento_form(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    form = AtendimentoForm(instance=Atendimento(paciente=paciente))
    return JsonResponse({
        'form': form.as_p()
    })

def teste(request):
    return render(request, 'prontuarios/teste-form.html')




def create_test(request):
    print('chamada func create_test')
    if request.method == 'POST':
        altura = request.POST['altura']
        peso = request.POST['peso']        
        paciente_id = request.POST['paciente_id']  # Obtenha o paciente_id do formulário

        try:
            paciente = Paciente.objects.get(pk=paciente_id)
        except Paciente.DoesNotExist:
            return HttpResponse('Paciente não encontrado')

        novo_atendimento = Atendimento(altura=altura, peso=peso, paciente=paciente)
        print('criado var novo_atendimento')

        try:
            novo_atendimento.full_clean()
            novo_atendimento.save()
            print('salvo var novo_atendimento')
            success = 'Profile created successfully for ' + altura
            print('dps var success')
            return HttpResponse(success)
        except Exception as e:
            print(f'Erro ao salvar o atendimento: {e}')
            return HttpResponse('Houve um erro ao salvar o atendimento')
    else:
        return HttpResponse('Método não permitido')
