from dashboard.models import Agendamento
from django import forms
from dashboard.models import Paciente, Convenio

class AgendamentoForm(forms.ModelForm):
    def __init__(self, *args, user, **kwargs):
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        
        self.fields['paciente'].queryset = Paciente.objects.filter(owner=user, show=True)
        self.fields['convenio'].queryset = Convenio.objects.filter(owner=user)
    class Meta:
        model = Agendamento
        fields = ['paciente', 'procedimento', 'convenio', 'data_consulta', 'hora_consulta', 'status']
