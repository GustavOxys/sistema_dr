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
                 'exame_fisico', 'altura', 'peso', 'diagnostico', 'condutas'
        '''widgets = {
            'queixa_principal' : forms.TextInput(attrs={'maxlength': 20}),
            'altura' : forms.TextInput(attrs={
                'maxlength': 4,
                'placeholder' : 'Ex: 1.70'
                })

        }'''

    def __init__(self, paciente_id, *args, **kwargs):
        super(AtendimentoForm, self).__init__(*args, **kwargs)
        self.paciente_id = paciente_id

    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error(
            None,
            ValidationError(
                'Ocorreu algum erro no Formulário, verifique os campos novamente',
                code='invalid'
            )
        )

    def clean_queixa_principal(self):
        queixa_principal = self.cleaned_data.get('queixa_principal')
        if queixa_principal is None:
            self.add_error(
                'queixa_principal',
                ValidationError(
                    'Esse campo é obrigatório',
                    code='campo_obrigatorio'                
                )
            )


    def clean_altura(self):
        altura = self.cleaned_data.get('altura')
        if altura is None:
            self.add_error(
                'altura',
                ValidationError(
                    'A altura é um campo obrigatório.',
                    code='campo_obrigatorio'
                )
            )

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso is None:
            self.add_error('peso', ValidationError('O peso é um campo Obrigatório', code='campo_obrigatorio'))


    

    
    
