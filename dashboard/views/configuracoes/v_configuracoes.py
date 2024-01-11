from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='dashboard:login')
def configuracoes(request):
    return render(request, 'configuracoes/configuracoes.html')