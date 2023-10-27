from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Procedimento(models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return self.nome

    

class Convenio(models.Model):
    nome = models.CharField(max_length=55)
    
    def __str__(self):
        return self.nome

class Paciente(models.Model):
    opcoes_sexo = [('Masculino', 'Masculino'),
                   ('Feminino', 'Feminino')]
    
    opcoes_status = [('Pendente', 'Pendente'),
                     ('Cancelado', 'Cancelado'),
                     ('Confirmado', 'Confirmado')]
    nome = models.CharField(max_length=55)
    telefone = models.CharField(max_length=30)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.DO_NOTHING)
    convenio = models.ForeignKey(Convenio, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_consulta = models.DateField(default='0000-00-00')
    hora_consulta = models.TimeField(default='09:00')
    observacao = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    show = models.BooleanField(default=True)
    email = models.EmailField(blank=True)
    data_nascimento = models.DateField(default='2000-01-01')    
    sexo_biologico = models.CharField(max_length=10, choices=opcoes_sexo, default='Masculino')
    cpf = models.CharField(max_length=13, blank=True, default='000000000-00')
    rg = models.CharField(max_length=15, blank=True, default='000000000000')
    nome_mae = models.CharField(max_length=55, blank=True, default='Desconhecido')
    cep = models.CharField(max_length=20, blank=True, default='00000-000')
    endereco = models.CharField(max_length=20, blank=True, default='Desconhecido')
    numero = models.CharField(max_length=20, blank=True, default='Desconhecido')    
    bairro = models.CharField(max_length=20, blank=True, default='Desconhecido')    
    cidade = models.CharField(max_length=20, blank=True, default='Desconhecido')
    estado = models.CharField(max_length=20, blank=True, default='Desconhecido')
    status = models.CharField(max_length=20, choices=opcoes_status, default='Pendente')


    

    def data_formatada(self):
        return self.data_consulta.strftime('%d/%m/%y')

    def __str__(self):
        return self.nome   