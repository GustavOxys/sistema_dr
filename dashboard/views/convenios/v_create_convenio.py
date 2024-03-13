from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from dashboard.forms.configuracoes.form_convenio import ConvenioForm
from django.contrib import messages

@login_required(login_url='dashboard:login')
def create_convenio(request): 
    form_action = reverse('dashboard:create_convenio')
    nome_func = 'Criar Convênio'

    if request.method == 'POST':
        form = ConvenioForm(request.POST)
        context = {
            'form' : form,
            'form_action': form_action
        }

        if form.is_valid():
            convenio = form.save(commit=False)
            convenio.owner = request.user
            convenio.save()
            messages.success(request, 'Convenio criado com sucesso!')
            return redirect('dashboard:convenios')
        else:
            messages.error(request, 'Ocorreu algum erro ao enviar o formulário')  
            return render(request, 'configuracoes/convenios/create_convenio.html', context) 
            
    context = {
        'form' : ConvenioForm(),
        'form_action' :form_action,
        'nome_func' : nome_func
    }

    return render(request, 'configuracoes/convenios/create_convenio.html', context)