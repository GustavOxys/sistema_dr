from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='dashboard:login_or_register')
def logout_user(request):
    auth.logout(request)
    return redirect('dashboard:login_or_register')