from django.shortcuts import render, redirect
from dashboard.forms.usuarios.form_user import RegisterForm
from django.core.exceptions import ValidationError
from django.contrib import messages


def register_user(request): 
    
     
    if request.method == 'POST':        
        form = RegisterForm(request.POST)
        if form.is_valid():            
            form.save()
            messages.success(request, 'Usuário registrado com sucesso!')  
            return redirect('dashboard:index')          
        
        else:
            messages.error(request, 'Ocorreu algum erro ao enviar o formulário')  
            return render(request, 'usuarios/register.html', {'form': form}) 
        
        


    form = RegisterForm()
    context = {
        'form': form
    }      
    return render(request, 'usuarios/register.html', context)
