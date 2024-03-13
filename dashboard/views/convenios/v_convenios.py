from dashboard.models import Convenio
from django.shortcuts import render, reverse, get_object_or_404, get_list_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from dashboard.forms.configuracoes.form_convenio import ConvenioForm
from django.contrib import messages


@login_required(login_url='dashboard:login')
def convenios(request):
    convenios = Convenio.objects.all().order_by('id')

    paginator = Paginator(convenios, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'convenios' : convenios,
        'page_obj' : page_obj
    }

    return render(request, 'configuracoes/convenios.html', context)

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
            messages.success(request, 'Convenio adicionado com sucesso!')
            return redirect('dashboard:convenios')
        else:
            messages.error(request, 'Ocorreu algum erro ao enviar o formulário')  
            return render(request, 'configuracoes/convenios.html', context) 
            
    context = {
        'form' : ConvenioForm(),
        'form_action' :form_action,
        'nome_func' : nome_func
    }

    return render(request, 'configuracoes/convenios.html', context)



@login_required(login_url='dashboard:login')
def update_convenio(request, convenio_id): 
    convenio = get_object_or_404(Convenio, pk=convenio_id)
    form_action = reverse('dashboard:update.convenio', args=(convenio_id,))
    nome_func = 'Editar Convenio'

    if request.method == 'POST':
        print('metodo é post convenio')
        form = ConvenioForm(request.POST, instance=convenio)
        context = {
            'form' : form,
            'form_action': form_action,
            'nome_func' : nome_func
        }

        if form.is_valid():
            convenio = form.save(commit=False)
            convenio.owner = request.user
            convenio.save()
            messages.success(request, 'Convenio editado com sucesso!')
            return redirect('dashboard:convenios')
        else:
            messages.error(request, 'Ocorreu algum erro ao salvar o formulário')  
            return render(request, 'configuracoes/convenios.html', context) 
    print('passou direto pelo if post convenio')  

    context = {
        'form' : ConvenioForm(instance=convenio),
        'form_action' :form_action,
        'nome_func' : nome_func
    }

    return render(request, 'configuracoes/convenios.html', context)


@login_required(login_url='dashboard:login')
def delete_convenio(request, convenio_id): 
    convenio = get_object_or_404(Convenio, pk=convenio_id)
    print(convenio)
    convenio.delete()

    return redirect('dashboard:convenios')