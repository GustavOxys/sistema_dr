from dashboard.models import Agendamento
from dashboard.models import Paciente, Convenio
from django import forms

class AgendamentoForm(forms.ModelForm):
    data_consulta = forms.DateField(
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder' : 'dd/mm/aaaa'}
        )
    )

    hora_consulta = forms.TimeField(
        widget=forms.TimeInput(
            format='%H:%M',
            attrs={'placeholder': 'hh:mm'}
        )
    ) 

    class Meta:
        model = Agendamento
        fields = ['paciente', 'procedimento', 'convenio', 'data_consulta', 'hora_consulta', 'status']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        
        self.fields['paciente'].queryset = Paciente.objects.filter(owner=user, show=True)
        self.fields['convenio'].queryset = Convenio.objects.filter(owner=user)
