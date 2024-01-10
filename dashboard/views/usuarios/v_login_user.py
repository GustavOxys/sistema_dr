from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth


def login_user(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)            
            return redirect('dashboard:index')
    
        messages.error(request, 'Login Inválido')

        
    return render(request, 'usuarios/login.html', {'form' : form})
