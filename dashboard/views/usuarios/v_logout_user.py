from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth


def logout_user(request):
    auth.logout(request)
    return redirect('dashboard:login')