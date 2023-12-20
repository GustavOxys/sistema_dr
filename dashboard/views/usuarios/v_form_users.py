from django.shortcuts import render
from dashboard.forms.usuarios.form_user import RegisterForm


def register_user(request):    
    form = RegisterForm()
    context = {
        'form' : form
    }      

    if request.method == 'POST':        
        form = RegisterForm(request.POST)
        if form.is_valid():            
            form.save()            
        else:
            print('erro ao salvar o formulario',)

    return render(request, 'usuarios/register.html', context)  
            
    