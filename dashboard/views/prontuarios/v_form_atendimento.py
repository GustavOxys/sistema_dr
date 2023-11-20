from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from dashboard.forms.atendimento.form_atendimento import AtendimentoForm

def atendimento_form(request, paciente_id):    
    form = AtendimentoForm()

    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'redirect_url': reverse('dashboard:prontuario', kwargs={'paciente_id': paciente_id})})

        return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'errors': form.errors})
