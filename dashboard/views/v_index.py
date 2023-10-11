from django.shortcuts import render
from dashboard.models import Paciente

app_name = 'index'


def index(request):

    pacientes = Paciente.objects.all()

    context = {
        'pacientes' : pacientes,
    }

    return render(request, 'index.html', context)
