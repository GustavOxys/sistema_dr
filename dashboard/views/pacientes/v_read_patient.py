from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Paciente
from dashboard.forms.pacientes.form_patient import PatientForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='dashboard:login')
def read_patient(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    return render(request, 'pacientes/read_patient.html', {'paciente' : paciente})