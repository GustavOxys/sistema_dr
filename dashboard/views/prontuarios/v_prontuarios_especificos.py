from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Atendimento
from django.core.paginator import Paginator


@login_required(login_url='dashboard:login')
def prontuarios_especificos(request, paciente_id):
    user = request.user

    prontuarios = Atendimento.objects\
        .filter(paciente__owner=user)\
        .filter(paciente__id=paciente_id)\
        .order_by('-data_hora_atendimento')

    for p in prontuarios:
        nome = p.paciente.nome      

    paginator = Paginator(prontuarios, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'prontuarios' : prontuarios,
        'nome' : nome,        
    }
    
    return render(request, 'prontuarios/prontuarios_especificos.html', context)