from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='dashboard:login')
def agenda(request):
    return render(request, 'agenda/agenda.html')