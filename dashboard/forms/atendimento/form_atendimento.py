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
        
    def __init__(self, paciente_id, *args, **kwargs):
        super(AtendimentoForm, self).__init__(*args, **kwargs)
        self.paciente_id = paciente_id

    

    def clean_queixa_principal(self):
        queixa_principal = self.cleaned_data.get('queixa_principal')

        if queixa_principal:
            if not any(char.isalpha() for char in queixa_principal):
                raise ValidationError('Este campo deve conter pelo menos uma letra.', code='letra_obrigatoria')

        return queixa_principal

    def clean(self):        
        queixa_principal = self.cleaned_data.get('queixa_principal')      
        

        if queixa_principal is None:
            self.add_error('queixa_principal', ValidationError('Esse campo é obrigatório',code='campo_obrigatorio'))

        

        if any(self.errors):
            self.add_error(None, ValidationError('Ocorreu algum erro no formulário, verifique os campos novamente', code='invalid'))


    

    

    
    
