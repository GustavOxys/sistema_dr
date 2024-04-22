from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Convenio
from django.contrib.auth.decorators import login_required


@login_required(login_url='dashboard:login_or_register')
def read_convenio(request, convenio_id):
    convenio = get_object_or_404(Convenio, pk=convenio_id)
    return render(request, 'configuracoes/convenios/read_convenio.html', {'convenio' : convenio})