from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='',        
        max_length=150,
        error_messages={},
        widget=forms.TextInput(attrs={
            'placeholder' : 'Nome de usuário',
            'class' : 'form'
            })
    )
    email = forms.EmailField(
        label='',
        error_messages={},
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class' : 'form'})
        )
    password1 = forms.CharField(
        label='',
        strip=False, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class' : 'form'}),
        error_messages={},
        
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder' : 'Confirme a senha', 'class' : 'form'}),
        strip=False,
        error_messages={},
    )

    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
