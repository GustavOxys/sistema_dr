from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Convenio
from dashboard.forms.configuracoes.form_convenio import ConvenioForm

@login_required(login_url='dashboard:login_or_register')
def configuracoes(request):
    convenios = Convenio.objects.all()
    if request.method == 'POST':
        form = ConvenioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:index')
    else:
        form = ConvenioForm()
    context = {'convenios' : convenios}
    
    return render(request, 'configuracoes/configuracoes.html', context)