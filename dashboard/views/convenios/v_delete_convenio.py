from django.shortcuts import redirect, get_object_or_404
from dashboard.models import Convenio
from dashboard.forms.configuracoes.form_convenio import ConvenioForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='dashboard:login')
def delete_convenio(request, convenio_id): 
    convenio = get_object_or_404(Convenio, pk=convenio_id)    
    convenio.delete()
    return redirect('dashboard:convenios')