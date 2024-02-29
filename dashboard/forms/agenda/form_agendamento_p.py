from dashboard.models import Agendamento
from django import forms
from dashboard.models import Paciente

class AgendamentoFormP(forms.ModelForm):

    def __init__(self, paciente_id, *args, **kwargs):
        super(AgendamentoFormP, self).__init__(*args, **kwargs)
        self.paciente_id = paciente_id

    class Meta:
        model = Agendamento
        fields = 'procedimento', 'convenio', 'data_consulta', 'hora_consulta', 'status'
