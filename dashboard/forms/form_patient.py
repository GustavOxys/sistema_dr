from django.shortcuts import render
from dashboard.models import Paciente
from django import forms

class PatientForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = 'nome', 'data_nascimento', 'sexo_biologico', 'cpf', 'rg', 'nome_mae', 'email',\
        'cep','endereco','numero', 'bairro', 'cidade', 'estado' ,'telefone', 'procedimento',\
        'convenio', 'data_consulta', 'hora_consulta', 'status'\

    widgets = {
        'hora_consulta' : forms.TextInput(
            attrs={
                'placeholder' : '00:00'
            }
        )
    }


