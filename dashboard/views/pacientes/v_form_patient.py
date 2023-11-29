from django.shortcuts import render, redirect
from dashboard.models import Paciente
from dashboard.forms.form_patient import PatientForm

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