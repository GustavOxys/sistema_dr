from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from dashboard.forms.usuarios.form_user import RegisterForm

def login_or_register(request):
    if request.method == 'POST':
        if 'login_form' in request.POST:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return JsonResponse({'success': True, 'redirect_url': '/dashboard/'})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        elif 'register_form' in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return JsonResponse({'success': True, 'redirect_url': '/dashboard/'})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        login_form = AuthenticationForm()
        register_form = RegisterForm()
        return render(request, 'usuarios/login_or_register.html', {'login_form': login_form, 'register_form': register_form})
