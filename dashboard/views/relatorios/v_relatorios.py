from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='dashboard:login_or_register')
def relatorios(request):
    return render(request, 'relatorios/relatorios.html')