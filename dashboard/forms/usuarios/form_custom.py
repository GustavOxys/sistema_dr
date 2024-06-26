from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nome de usuário'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Senha'
        })

