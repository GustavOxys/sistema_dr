from django import forms
from dashboard.models import Convenio

class ConvenioForm(forms.ModelForm):
    class Meta:
        model = Convenio
        fields = ['valor_padrao']
