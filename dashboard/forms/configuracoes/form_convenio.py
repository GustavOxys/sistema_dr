from django import forms
from dashboard.models import Convenio

class ConvenioForm(forms.ModelForm):
    class Meta:
        model = Convenio
        fields = 'nome', 'valor_padrao', 'n_reconsultas', 'prazo_reconsultas',
