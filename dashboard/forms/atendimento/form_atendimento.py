from dashboard.models import Atendimento
from django import forms


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = 'queixa_principal', 'historia_molestia_atual', 'historico_e_antecedentes', \
                 'exame_fisico', 'altura', 'peso', 'diagnostico', 'condutas'

    def __init__(self, paciente_id, *args, **kwargs):
        super(AtendimentoForm, self).__init__(*args, **kwargs)
        self.paciente_id = paciente_id
