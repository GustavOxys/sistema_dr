from dashboard.models import Convenio
from django.shortcuts import render, reverse, get_object_or_404, get_list_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from dashboard.forms.configuracoes.form_convenio import ConvenioForm
from django.contrib import messages


@login_required(login_url='dashboard:login')
def convenios(request):
    user = request.user
    convenios = Convenio.objects.filter(owner=user).order_by('id')
    print(convenios)
    for c in convenios:
        print('conv', c)

    paginator = Paginator(convenios, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'convenios' : convenios,
        'page_obj' : page_obj
    }

    return render(request, 'configuracoes/convenios.html', context)

