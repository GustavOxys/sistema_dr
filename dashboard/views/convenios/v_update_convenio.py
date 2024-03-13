from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms.configuracoes.form_convenio import ConvenioForm
from dashboard.models import Convenio

def update_convenio(request, convenio_id):
    convenio = get_object_or_404(Convenio, pk=convenio_id)
    nome_func = 'Editar Convênio'

    if request.method == 'POST':
        form = ConvenioForm(request.POST, instance=convenio)
        context = {
            'form' : form,
            'nome_func' : nome_func
        }
        if form.is_valid():
            convenio = form.save(commit=False)
            convenio.owner = request.user
            convenio.save()
            return redirect('dashboard:convenios')

    form = ConvenioForm(instance=convenio)

    context = {
        'form' : form,
        'nome_func' : nome_func,
    }
    return render(request, 'configuracoes/convenios/create_convenio.html', context)