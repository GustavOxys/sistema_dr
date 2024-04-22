from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from dashboard.forms.usuarios.form_user import RegisterForm
from dashboard.forms.usuarios.form_custom import CustomAuthenticationForm
from icecream import ic
from dashboard.models import Convenio, Procedimento


def login_or_register(request):
    success = request.session.pop('success', None)     
    if request.method == 'POST':        
        form_type = request.POST.get('form_type')        
        if form_type == 'login':            
            form = CustomAuthenticationForm(request, data=request.POST)
            if form.is_valid():                
                user = form.get_user()
                login(request, user)
                return redirect('dashboard:index')
            else:
                messages.error(request, 'Usuário ou senha incorreto, Verifique seu usuário e senha ou crie uma conta') 
                request.session['success'] = True 
                return redirect('dashboard:login_or_register') 

        if form_type == 'register':            
            form = RegisterForm(request.POST)
            if form.is_valid():                
                user = form.save()  
                convenio = Convenio.objects.create(owner=user, nome="Particular")
                procedimento = Procedimento.objects.create(owner=user, nome='Consulta')              
                messages.success(request, 'Usuário registrado com sucesso!') 
                request.session['success'] = True                
                return redirect('dashboard:login_or_register') 
            else:                
                messages.error(request, 'Ocorreu algum erro ao enviar o formulário')                                
                return redirect('dashboard:login_or_register') 
        else:
            ic()

    login_form = CustomAuthenticationForm(request)
    register_form = RegisterForm()   
    
    context = {
        'login_form' : login_form,
        'register_form' : register_form,
        'success' : success
    }
    
    return render(request, 'usuarios/login_or_register.html', context)
