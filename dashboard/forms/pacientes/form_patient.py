from dashboard.models import Paciente
from django import forms
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from icecream import ic



class PatientForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder' : 'dd/mm/aaaa'},
        ),      
    )
    nome = forms.CharField(
        max_length=100,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Por favor, insira apenas letras.')])

    telefone = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\(\d{2}\)\d\s\d{4}-\d{4}$',
                message='O número de telefone deve estar no formato (XX)X XXXX-XXXX',
            ),
        ],
    )
    


    cpf = forms.CharField(
        label='CPF',
        max_length=14,
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
                message='O CPF deve estar no formato XXX.XXX.XXX-XX',
                code='invalid_cpf'
            )
        ]
    )

    
    class Meta:
        model = Paciente
        fields = 'nome', 'data_nascimento',  'cpf', 'telefone', 'rg',\
        'nome_mae', 'email', 'cep','endereco','numero', 'bairro', 'cidade', 'estado' , 'sexo_biologico',
            
    def clean_cpf(self):
        
        cpf = self.cleaned_data.get('cpf')
        cpf_limpo = re.sub(r'\D', '', cpf)
        
        if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
            self.add_error('cpf_limpo', ValidationError("CPF deve conter 11 dígitos numéricos.", code='invalid'))  
        
        nove_digitos = cpf_limpo[:9]
        contador_regressivo_1 = 10
        resultado_digito_1 = 0
        
        for digito in nove_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1

        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11
        resultado_digito_2 = 0

        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1

        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'        
        
        # Verifica se o CPF calculado é igual ao informado
        if cpf_limpo != cpf_calculado:
            self.add_error('cpf', ValidationError("CPF Inválido.", code='invalid'))        
        return cpf
        


