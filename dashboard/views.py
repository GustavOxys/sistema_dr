from django.shortcuts import render

app_name = 'index'


def index(request):
    return render(request, 'index.html')
