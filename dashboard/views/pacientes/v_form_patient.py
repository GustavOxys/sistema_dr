from django.shortcuts import render, redirect
from dashboard.models import Paciente
from dashboard.forms.pacientes.form_patient import PatientForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib import messages




@login_required(login_url='dashboard:login')
def create(request):    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        context = {
        'form' : form
        }

        
        if form.is_valid():
            patient = form.save(commit=False)
            patient.owner = request.user
            patient.save()
            messages.success(request, 'Paciente adicionado com sucesso!')
            return redirect('dashboard:pacientes')
        else:
            messages.error(request, 'Ocorreu algum erro ao enviar o formulário')  
            return render(request, 'pacientes/create.html', context)
                
        

        

    
    context = {
        'form' : PatientForm()
    }

    return render(request, 'pacientes/create.html', context)