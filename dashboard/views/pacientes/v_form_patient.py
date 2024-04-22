from django.shortcuts import render, redirect
from dashboard.models import Paciente
from dashboard.forms.pacientes.form_patient import PatientForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.urls import reverse
from icecream import ic


@login_required(login_url='dashboard:login_or_register')
def create(request): 
    ic()
    form_action = reverse('dashboard:create')
    nome_func = 'Registrar Paciente'

    if request.method == 'POST':
        ic()
        form = PatientForm(request.POST)
        context = {
            'form' : form,
            'form_action': form_action
        }

        if form.is_valid():
            ic()
            patient = form.save(commit=False)
            patient.owner = request.user
            patient.save()
            messages.success(request, 'Paciente adicionado com sucesso!')
            return redirect('dashboard:pacientes')
        else:
            ic()
            messages.error(request, 'Ocorreu algum erro ao enviar o formulário')  
            return render(request, 'pacientes/create.html', context) 
    ic()        
    context = {
        'form' : PatientForm(),
        'form_action' :form_action,
        'nome_func' : nome_func
    }

    return render(request, 'pacientes/create.html', context)
            

            

    

     
        

        