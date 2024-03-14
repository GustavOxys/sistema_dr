from dashboard.models import Agendamento
from django import forms
from dashboard.models import Paciente, Convenio

class AgendamentoFormP(forms.ModelForm):

    def __init__(self, paciente_id, user, *args, **kwargs):
        super(AgendamentoFormP, self).__init__(*args, **kwargs)
        self.paciente_id = paciente_id
        self.fields['convenio'].queryset = Convenio.objects.filter(owner=user)
    class Meta:
        model = Agendamento
        fields = 'procedimento', 'convenio', 'data_consulta', 'hora_consulta', 'status'
