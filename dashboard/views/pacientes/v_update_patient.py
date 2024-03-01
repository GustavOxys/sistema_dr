from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Paciente
from dashboard.forms.pacientes.form_patient import PatientForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


@login_required(login_url='dashboard:login')
def update_patient(request, paciente_id): 
    patient = get_object_or_404(Paciente, pk=paciente_id, show=True)
    form_action = reverse('dashboard:update_patient', args=(paciente_id,))

    if request.method == 'POST':
        print('metodo é post patient')
        form = PatientForm(request.POST, instance=patient)
        context = {
            'form' : form,
            'form_action': form_action
        }

        if form.is_valid():
            patient = form.save(commit=False)
            patient.owner = request.user
            patient.save()
            messages.success(request, 'Paciente editado com sucesso!')
            return redirect('dashboard:pacientes')
        else:
            messages.error(request, 'Ocorreu algum erro ao salvar o formulário')  
            return render(request, 'pacientes/create.html', context) 
    print('passou direto pelo if post patient')        
    context = {
        'form' : PatientForm(instance=patient),
        'form_action' :form_action
    }

    return render(request, 'pacientes/create.html', context)
            

            

    

     
        

        