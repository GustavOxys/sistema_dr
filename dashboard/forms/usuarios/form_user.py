from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.core.validators import RegexValidator


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        validators=[RegexValidator(r'^[a-zA-Z]*$', 'Por favor, insira apenas letras.')],
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        validators=[RegexValidator(r'^[a-zA-Z]*$', 'Por favor, insira apenas letras.')],
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )

        return email

    