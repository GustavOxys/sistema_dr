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
    
    def __str__(self):
        return self.nome

    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))
    

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
    data_atendimento = models.DateTimeField(default=timezone.localdate())


    def save(self, *args, **kwargs):
        print('dentro do metodo save')
        hoje = timezone.now()        
        print(hoje)
        if self.data_atendimento == hoje.date():
            self.total_diario += 1
            print('total diario', self.total_diario)
        else:
            self.self.total_diario = 1
            print('total diario else', self.total_diario)

        if self.data_atendimento.month == hoje.month:
            self.total_mensal += 1
            print('total mensal', self.total_mensal)
        else:
            self.self.total_mensal = 1
            print('total mensal else', self.total_mensal)

        if self.data_atendimento.year == hoje.year:
            self.total_anual += 1
            print('total anual', self.total_anual)
        else:
            self.self.total_anual = 1
            print('total anual else', self.total_anual)
        super().save(*args, **kwargs)   


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
    total_diario = models.IntegerField(default=0)
    total_mensal = models.IntegerField(default=0)
    total_anual = models.IntegerField(default=0)
    data_agendamento = models.DateTimeField(default=timezone.localdate())

    def save(self, *args, **kwargs):
        print('dentro do metodo save agendamento')
        hoje = timezone.now()        
        print(hoje)
        if self.data_agendamento == hoje.date():
            self.total_diario += 1
            print('total diario', self.total_diario)
        else:
            self.self.total_diario = 1
            print('total diario else', self.total_diario)

        if self.data_agendamento.month == hoje.month:
            self.total_mensal += 1
            print('total mensal', self.total_mensal)
        else:
            self.self.total_mensal = 1
            print('total mensal else', self.total_mensal)

        if self.data_agendamento.year == hoje.year:
            self.total_anual += 1
            print('total anual', self.total_anual)
        else:
            self.self.total_anual = 1
            print('total anual else', self.total_anual)
        super().save(*args, **kwargs) 


    def data_formatada(self):
        return self.data_consulta.strftime('%d/%m/%y')

    



