from django.shortcuts import render, redirect
from dashboard.models import Paciente
from dashboard.forms.pacientes.form_patient import PatientForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib import messages




@login_required(login_url='dashboard:login')
def create(request): 
    print('dentro da func create')   
    if request.method == 'POST':
        print('se o metodo é post')
        form = PatientForm(request.POST)
        context = {
        'form' : form
        }

        
        if form.is_valid():
            print('cpf is valid')
            patient = form.save(commit=False)
            patient.owner = request.user
            print('patient owner é o usuario')

            patient.save()
            print('dados salvos')
            messages.success(request, 'Paciente adicionado com sucesso!')
            return redirect('dashboard:pacientes')
        else:
            messages.error(request, 'Ocorreu algum erro ao enviar o formulário')  
            return render(request, 'pacientes/create.html', context) 

    
    context = {
        'form' : PatientForm()
    }

    return render(request, 'pacientes/create.html', context)