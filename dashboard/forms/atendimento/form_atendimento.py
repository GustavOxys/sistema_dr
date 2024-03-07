from dashboard.models import Atendimento
from django import forms
from django.core.exceptions import ValidationError


class AtendimentoForm(forms.ModelForm):
    altura = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder' : 'Ex: 1.60'}
        ),
        help_text='Altura em Metros'
    )

    queixa_principal = forms.CharField(
        widget=forms.TextInput(
            attrs={'maxlength' : 30}
        )
    )

    peso = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder' : 'Ex: 60'}
        ),
        help_text='Peso em Kg'
    )
    

    class Meta:
        model = Atendimento
        fields = 'queixa_principal', 'historia_molestia_atual', 'historico_e_antecedentes', \
                 'exame_fisico', 'altura', 'peso', 'diagnostico', 'condutas', 
        
    def __init__(self, *args, agendamento_id=None, user=None, **kwargs):
        super(AtendimentoForm, self).__init__(*args, **kwargs)
        self.agendamento_id = agendamento_id

    

    

    

    

    
    
