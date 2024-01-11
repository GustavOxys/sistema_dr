from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import password_validation


class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=30,
        help_text='Obrigatório.',
        error_messages={
            'min_length' : 'Por favor, adicione mais que 2 letras.'
        }
    )

    last_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=30,
        help_text='Obrigatório.',
    )

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete' : 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label='Password 2',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete' : 'new-password'}),
        help_text='Use a mesma senha de antes.',
        required=False,
    )
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()
        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('As senhas devem ser iguais.')
                )




    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1',
                ValidationError(errors)
                )

        return password1
