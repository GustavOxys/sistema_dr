from django.shortcuts import render
from dashboard.forms.usuarios.form_user import RegisterForm
from django.core.exceptions import ValidationError

def register_user(request):    
    if request.method == 'POST':        
        form = RegisterForm(request.POST)
        if form.is_valid():            
            form.save()
            success_message = 'Usuário registrado com sucesso!'
            return render(request, 'usuarios/register.html', {'form': form, 'success_message': success_message})
        else:
            error_message = 'Ocorreu algum erro ao enviar o formulário'
            return render(request, 'usuarios/register.html', {'form': form, 'error_message': error_message})

    form = RegisterForm()
    context = {
        'form': form
    }      
    return render(request, 'usuarios/register.html', context)
