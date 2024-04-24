from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    


    username = forms.CharField(                
        max_length=15,
        min_length=4,
        required=True,               
        widget=forms.TextInput(attrs={
            'placeholder' : 'Nome de usuário',
            'class' : 'form'
            })
    )

    
    email = forms.EmailField(
        required=True,
        min_length=10,
        max_length=50,              
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class' : 'form'})
        )

    password1 = forms.CharField(
        label='',
        strip=False, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class' : 'form'}),        
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder' : 'Confirme a senha', 'class' : 'form'}),
        strip=False,
        
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    
