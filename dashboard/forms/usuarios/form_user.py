from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        error_messages={},
        widget=forms.TextInput(attrs={'placeholder' : 'Nome de usuário'})
    )
    email = forms.EmailField(
        error_messages={},
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail'})
        )
    password1 = forms.CharField(
        label="Senha",
        strip=False, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
        error_messages={},
        
    )
    password2 = forms.CharField(
        label="Confirmação de Senha",
        widget=forms.PasswordInput(attrs={'placeholder' : 'Confirme a senha'}),
        strip=False,
        error_messages={},
    )

    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
