from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='dashboard:login')
def prontuarios(request):
    return render(request, 'prontuarios/prontuarios.html')