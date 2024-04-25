from dashboard.models import Atendimento
from django import forms
from django.core.exceptions import ValidationError


class AtendimentoForm(forms.ModelForm):
    altura = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder' : 'Ex: 1.60',
            'class' : 'form-atendimento-altura',
            'size': '10'},
        ),
        help_text='Altura em Metros',
    )

    queixa_principal = forms.CharField(
        widget=forms.TextInput(
            attrs={'maxlength' : 100}
        )
    )

    peso = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder' : 'Ex: 60'}
        ),
        help_text='Peso em Kgs'
    )
    

    class Meta:
        model = Atendimento
        fields = 'queixa_principal', 'altura', 'peso', 'historia_molestia_atual', 'historico_e_antecedentes', 'exame_fisico',  'diagnostico', 'condutas', 
        
    def __init__(self, *args, agendamento_id=None, user=None, **kwargs):
        super(AtendimentoForm, self).__init__(*args, **kwargs)
        self.agendamento_id = agendamento_id


    def clean_altura(self):
        altura = self.cleaned_data.get('altura')
        if altura is not None:
            try:
                float(altura)
            except ValueError:
                raise forms.ValidationError('A Altura deve conter apenas números')
        return altura

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso is not None:
            try:
                float(peso)
            except ValueError:
                raise forms.ValidationError('A peso deve conter apenas números')
        return peso
    
    

    

    

    

    
    
