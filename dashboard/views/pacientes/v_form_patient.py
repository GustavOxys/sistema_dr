from django.shortcuts import render, redirect
from dashboard.models import Paciente
from dashboard.forms.pacientes.form_patient import PatientForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='dashboard:login')
def create(request):    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        context = {
        'form' : form
        }

        if form.is_valid():
            form.save()
            return redirect('dashboard:create')
        return render(request, 'pacientes/create.html', context)

    
    context = {
        'form' : PatientForm()
    }

    return render(request, 'pacientes/create.html', context)