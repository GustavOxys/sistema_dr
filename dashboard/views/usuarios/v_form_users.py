from django.shortcuts import render
from dashboard.forms.usuarios.form_user import RegisterForm


def register_user(request):
    print('request do register user')
    form = RegisterForm()
    

    context = {
        'form' : form
    }
    print('context criado')

    if request.method == 'POST':
        print('se o metodo é post')
        form = RegisterForm(request.POST)
        print('form = registerform')

        if form.is_valid():
            print('se o form é valido')
            form.save()
            print('form salvo')
        else:
            print('erro ao salvar o formulario',)

            
    return render(
        request,
        'usuarios/register.html',
        context
    )