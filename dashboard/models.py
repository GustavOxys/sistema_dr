from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
import re
from django.core.exceptions import ValidationError



class Procedimento(models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return self.nome
    

class Convenio(models.Model):
    nome = models.CharField(max_length=55)
    
    def __str__(self):
        return self.nome
    

class Paciente(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    opcoes_sexo = [('Masculino', 'Masculino'),
                   ('Feminino', 'Feminino')]
    
    
    nome = models.CharField(max_length=55)
    idade = models.CharField(max_length=2, blank=True, default=18)
    telefone = models.CharField(max_length=30)    
    data_criacao = models.DateTimeField(default=timezone.now)    
    observacao = models.TextField(blank=True)    
    show = models.BooleanField(default=True)
    email = models.EmailField(blank=True)
    data_nascimento = models.DateField(null=False)    
    sexo_biologico = models.CharField(max_length=10, choices=opcoes_sexo, null=False)
    cpf = models.CharField(max_length=14, null=False)
    rg = models.CharField(max_length=15, blank=True, default='000000000000')
    nome_mae = models.CharField(max_length=55, blank=True, default='Desconhecido')
    cep = models.CharField(max_length=20, blank=True, default='00000-000')
    endereco = models.CharField(max_length=20, blank=True, default='Desconhecido')
    numero = models.CharField(max_length=20, blank=True, default='Desconhecido')    
    bairro = models.CharField(max_length=20, blank=True, default='Desconhecido')    
    cidade = models.CharField(max_length=20, blank=True, default='Desconhecido')
    estado = models.CharField(max_length=20, blank=True, default='Desconhecido')
    
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    
    

    def __str__(self):
        return self.nome   

    def clean(self):
        super().clean()
        # Remove caracteres não numéricos do CPF
        cpf = re.sub(r'\D', '', self.cpf)

        # Verifica se o CPF tem 11 dígitos
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValidationError("CPF deve conter 11 dígitos numéricos.")

        # Realiza o cálculo do CPF
        nove_digitos = cpf[:9]
        contador_regressivo_1 = 10
        resultado_digito_1 = 0

        for digito in nove_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1

        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11
        resultado_digito_2 = 0

        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1

        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

        # Verifica se o CPF calculado é igual ao informado
        if cpf != cpf_calculado:
            raise ValidationError("CPF inválido.")

    def save(self, *args, **kwargs):
        self.clean()  # Chama a função de validação antes de salvar
        super().save(*args, **kwargs)
    

class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    queixa_principal = models.TextField(max_length=20, blank=True)
    historia_molestia_atual = models.TextField(max_length=250, blank=True)
    historico_e_antecedentes = models.TextField(max_length=200, blank=True)
    exame_fisico = models.TextField(max_length=250, blank=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2, blank=True)  # Altura em metros
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True)  # Peso em quilogramas
    imc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    diagnostico = models.TextField(max_length=50, blank=True)
    condutas = models.TextField(max_length=250, blank=True)
    total_diario = models.IntegerField(default=0)
    total_mensal = models.IntegerField(default=0)
    total_anual = models.IntegerField(default=0)
    data_atendimento = models.DateTimeField(default=timezone.now())


    def adicionar_atendimento(self):
        hoje = timezone.now()        
        
        if self.data_atendimento.date() == hoje.date():
            self.total_diario += 1
        else:            
            self.total_diario = 1
            self.total_mensal += 1 if self.data_atendimento.month != hoje.month else 0
            self.total_anual += 1 if self.data_atendimento.year != hoje.year else 0

        self.save()   


    def saveimc(self, *args, **kwargs):
        if self.altura > 0 and self.peso > 0:
            # Realiza o cálculo do IMC
            self.imc = self.peso / (self.altura * self.altura)
        super(Atendimento, self).saveimc(*args, **kwargs)

    

class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    resumo = models.TextField(blank=True)
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE, related_name="prontuarios")



class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    data_consulta = models.DateField(default='0000-00-00')
    hora_consulta = models.TimeField(default='09:00')
    procedimento = models.ForeignKey(Procedimento, on_delete=models.DO_NOTHING)
    convenio = models.ForeignKey(Convenio, on_delete=models.DO_NOTHING)
    opcoes_status = [('Pendente', 'Pendente'),
                     ('Cancelado', 'Cancelado'),
                     ('Confirmado', 'Confirmado')]
    status = models.CharField(max_length=20, choices=opcoes_status, default='Pendente')


    def data_formatada(self):
        return self.data_consulta.strftime('%d/%m/%y')

    



