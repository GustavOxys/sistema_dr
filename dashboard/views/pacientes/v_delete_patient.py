from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Paciente
from dashboard.forms.pacientes.form_patient import PatientForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


@login_required(login_url='dashboard:login')
def delete_patient(request, paciente_id): 
    patient = get_object_or_404(Paciente, pk=paciente_id, show=True)
    print(patient)
    patient.delete()

    return redirect('dashboard:pacientes')