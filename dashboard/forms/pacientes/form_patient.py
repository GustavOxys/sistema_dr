from dashboard.models import Paciente
from django import forms
import re
from django.core.exceptions import ValidationError


class PatientForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        
    )
    class Meta:
        model = Paciente
        fields = 'nome', 'data_nascimento', 'sexo_biologico', 'cpf', 'rg', 'nome_mae', 'email',\
        'cep','endereco','numero', 'bairro', 'cidade', 'estado' ,'telefone',

    widgets = {
        'hora_consulta' : forms.TextInput(
            attrs={
                'placeholder' : '00:00'
            }
        )
    }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        print('pegou cpf enviado' ,cpf)

        cpf = re.sub(r'\D', '', cpf)
        print('pegou cpf enviado e fez a expressão regular', cpf)


        # Verifica se o CPF tem 11 dígitos
        if not cpf.isdigit() or len(cpf) != 11:
            print('verificou if o cpf é digitos e diferente de 11')

            self.add_error('cpf', ValidationError("CPF deve conter 11 dígitos numéricos.", code='invalid'))
            print('add_error, cpf invalido')


        # Realiza o cálculo do CPF
        nove_digitos = cpf[:9]
        contador_regressivo_1 = 10
        resultado_digito_1 = 0
        print('realizando calculo cpf')

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
        print(cpf_calculado)

        # Verifica se o CPF calculado é igual ao informado
        if cpf != cpf_calculado:
            self.add_error('cpf', ValidationError("CPF Inválido.", code='invalid'))
        
        return cpf


