from django.shortcuts import redirect, get_object_or_404
from dashboard.models import Paciente
from dashboard.forms.pacientes.form_patient import PatientForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='dashboard:login_or_register')
def delete_patient(request, paciente_id): 
    patient = get_object_or_404(Paciente, pk=paciente_id, show=True)
    print(patient)
    patient.delete()

    return redirect('dashboard:pacientes')