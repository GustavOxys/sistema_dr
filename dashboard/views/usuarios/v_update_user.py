from dashboard.forms.usuarios.form_update_register import RegisterUpdateForm
from django.shortcuts import render, redirect

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'usuarios/update_user.html',
            {
                'form' : form
            }
        )
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'usuarios/update_user.html',
            {
                'form' : form
            }
        )
    
    form.save()
    return redirect('dashboard:user_update')