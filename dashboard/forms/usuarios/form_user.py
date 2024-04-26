from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm): 
    username = forms.CharField(                
        required=True,               
        min_length=4,
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Nome de usuário', 'class' : 'form'})
    )   

    email = forms.EmailField(
        required=True,
        min_length=10,
        max_length=50,              
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class' : 'form'})
        )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class' : 'form'}),        
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder' : 'Confirme a senha', 'class' : 'form'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Esse Usuário ja está em uso')
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Esse email já está em uso')
        else:
            return email