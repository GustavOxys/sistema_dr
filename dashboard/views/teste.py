from django.shortcuts import render
from django import forms
from dashboard.models import Atendimento
from django.core.exceptions import ValidationError

class TesteForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields =  'queixa_principal', 'historia_molestia_atual', 'historico_e_antecedentes', \
                 'exame_fisico', 'altura', 'peso', 'diagnostico', 'condutas',

    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            'queixa_principal',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        return super().clean()

def teste(request):
    if request.method == 'POST':
        context = {
        'form' : TesteForm(request.POST)
        }
    
        return render(request, 'teste.html', context)

    context = {
            'form' : TesteForm()
        }
    return render(request, 'teste.html', context)