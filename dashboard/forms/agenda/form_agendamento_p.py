from dashboard.models import Agendamento
from dashboard.models import Paciente, Convenio
from django import forms
from django.core.validators import RegexValidator

class AgendamentoFormP(forms.ModelForm):        
    data_consulta = forms.DateField(
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs= {'placeholder' : 'dd/mm/aaaa'}
        ),        
    )

    hora_consulta = forms.TimeField(
        widget=forms.TimeInput(
            format='%H:%M',
            attrs={'placeholder': 'hh:mm'}
        )
    )    

    class Meta:
        model = Agendamento
        fields = ['procedimento', 'convenio', 'data_consulta', 'hora_consulta', 'status']

    def __init__(self, paciente_id, user, *args, **kwargs):
        super(AgendamentoFormP, self).__init__(*args, **kwargs)
        self.paciente_id = paciente_id
        self.fields['convenio'].queryset = Convenio.objects.filter(owner=user)
        
    


