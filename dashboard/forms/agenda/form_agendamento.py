from dashboard.models import Agendamento
from django import forms
from dashboard.models import Paciente

class AgendamentoForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['paciente'].queryset = Paciente.objects.filter(owner=user, show=True)

    class Meta:
        model = Agendamento
        fields = ['paciente', 'procedimento', 'convenio', 'data_consulta', 'hora_consulta', 'status']
