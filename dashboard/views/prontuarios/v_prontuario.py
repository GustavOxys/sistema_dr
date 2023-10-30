from django.shortcuts import render

def prontuario(request):
    return render(request, 'prontuarios/prontuario.html')