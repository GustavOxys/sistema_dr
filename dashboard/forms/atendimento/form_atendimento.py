from dashboard.models import Atendimento
from django import forms

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = 'queixa_principal', 'historia_molestia_atual', 'historico_e_antecedentes',\
        'exame_fisico', 'altura', 'peso', 'imc', 'diagnostico', 'condutas', 

    