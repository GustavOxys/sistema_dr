from dashboard.models import Agendamento
from dashboard.models import Paciente, Convenio
from django import forms

class AgendamentoForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        
        self.fields['paciente'].queryset = Paciente.objects.filter(owner=user, show=True)
        self.fields['convenio'].queryset = Convenio.objects.filter(owner=user)
    class Meta:
        model = Agendamento
        fields = ['paciente', 'procedimento', 'convenio', 'data_consulta', 'hora_consulta', 'status']
