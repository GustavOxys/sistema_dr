from django.shortcuts import render
from dashboard.models import Paciente
from django import forms

class PatientForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = 'nome', 'telefone', 'procedimento',\
        'convenio', 'data_consulta', 'hora_consulta', 'observacao',

    widgets = {
        'hora_consulta' : forms.TextInput(
            attrs={
                'placeholder' : '00:00'
            }
        )
    }


