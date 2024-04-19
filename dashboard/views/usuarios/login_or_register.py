from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from dashboard.forms.usuarios.form_user import RegisterForm
from dashboard.forms.usuarios.form_custom import CustomAuthenticationForm
from icecream import ic

def login_or_register(request):
    if request.method == 'POST':
        ic()
        ic(request.POST)
        form_type = request.POST.get('form_type')
        ic(form_type)
        if form_type == 'login':
            ic()
            form = CustomAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                ic()
                user = form.get_user()
                login(request, user)
                return redirect('dashboard:index')
            else:
                ic()
                return JsonResponse({'success': False, 'errors': form.errors})
        if form_type == 'register':
            ic()
            form = RegisterForm(request.POST)
            if form.is_valid():
                ic()
                user = form.save()
                
                messages.success(request, 'Usuário registrado com sucesso!') 
                
                return redirect('dashboard:login_or_register') 
            else:
                ic()
                messages.error(request, 'Ocorreu algum erro ao enviar o formulário') 
                return redirect('dashboard:login_or_register') 
        else:
            ic()
    else:
        ic()
        login_form = CustomAuthenticationForm(request)
        register_form = RegisterForm()
        ic(login_form)
        ic(register_form)
        
        context = {
            'login_form' : login_form,
            'register_form' : register_form,
        }
        return render(request, 'usuarios/login_or_register.html', context)
