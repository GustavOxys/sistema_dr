from django.shortcuts import render
from dashboard.models import Paciente
from dashboard.forms.form_patient import PatientForm

def create(request):    
    if request.method == 'POST':
        context = {
        'form' : PatientForm(request.POST)
        }

        return render(request, 'dashboard/create.html', context)

    
    context = {
        'form' : PatientForm()
    }

    return render(request, 'dashboard/create.html', context)