from django.shortcuts import render

def prontuarios(request):
    return render(request, 'prontuarios/prontuarios.html')