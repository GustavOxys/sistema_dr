from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
import re
from django.core.exceptions import ValidationError
from datetime import timedelta


class Procedimento(models.Model):
    nome = models.CharField(max_length=55)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome
    

class Convenio(models.Model):
    shared_choices = [
        ('Particular', 'Particular'),
        ('Unimed', 'Unimed'),
        ('SUS', 'SUS')
    ]
    shared_value = models.CharField(max_length=20, choices=shared_choices, default='Particular')    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=55)
    valor_padrao = models.DecimalField(default=50.00, max_digits=10, decimal_places=2)
    n_reconsultas = models.CharField(max_length=10, default=3)
    prazo_reconsultas = models.CharField(max_length=30, default=15)

    def __str__(self):
        return self.nome
    

class Paciente(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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

    def calcular_idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))    

    def save(self, *args, **kwargs):
        self.idade = self.calcular_idade()
        self.clean()  # Chama a função de validação antes de salvar
        super().save(*args, **kwargs)
    
class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    atendido = models.BooleanField(default=False)
    data_consulta = models.DateField(default='0000-00-00')
    hora_consulta = models.TimeField(default='09:00')
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    opcoes_status = [('Pendente', 'Pendente'),
                     ('Cancelado', 'Cancelado'),
                     ('Confirmado', 'Confirmado')]
    status = models.CharField(max_length=20, choices=opcoes_status, default='Pendente')
    total_diario = models.IntegerField(default=0)
    total_mensal = models.IntegerField(default=0)
    total_anual = models.IntegerField(default=0)
    data_agendamento = models.DateTimeField(default=timezone.localdate())
    data_hora_agendamento = models.DateTimeField(default=timezone.now() - timedelta(hours=3) )

    def save(self, *args, **kwargs):        
        hoje = timezone.now()       
        
        if self.data_agendamento == hoje.date():
            self.total_diario += 1            
        else:
            self.total_diario = 1            

        if self.data_agendamento.month == hoje.month:
            self.total_mensal += 1            
        else:
            self.total_mensal = 1            

        if self.data_agendamento.year == hoje.year:
            self.total_anual += 1            
        else:
            self.total_anual = 1
            
        super().save(*args, **kwargs) 


    def data_formatada(self):
        return self.data_consulta.strftime('%d/%m/%y')



class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)     
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, null=True, blank=True)  
    atendido = models.BooleanField(default=False)
    queixa_principal = models.TextField(max_length=20, blank=True, null=True)
    historia_molestia_atual = models.TextField(max_length=250, blank=True)
    historico_e_antecedentes = models.TextField(max_length=200, blank=True)
    exame_fisico = models.TextField(max_length=250, blank=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)# Altura em metros
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)# Peso em quilogramas
    imc = models.FloatField(null=True, blank=True)
    diagnostico = models.TextField(max_length=50, blank=True)
    condutas = models.TextField(max_length=250, blank=True)
    total_diario = models.IntegerField(default=0)
    total_mensal = models.IntegerField(default=0)
    total_anual = models.IntegerField(default=0)
    data_atendimento = models.DateField(default=timezone.localdate)
    data_hora_atendimento = models.DateTimeField(default=timezone.now())
    editado = models.BooleanField(default=False)
    valor_total_diario = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    valor_total_mensal = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    valor_total_anual = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    

    def save(self, *args, **kwargs):        
        hoje = timezone.now()        
        
        if self.editado == False:
            if self.data_atendimento == hoje.date:
                self.total_diario += 1                
            else:
                self.total_diario = 1
                

            if self.data_atendimento.month == hoje.month:
                self.total_mensal += 1                
            else:
                self.total_mensal = 1
                

            if self.data_atendimento.year == hoje.year:
                self.total_anual += 1                
            else:
                self.total_anual = 1

        if self.agendamento.procedimento.nome == 'Consulta':
            if self.data_atendimento == hoje.date:
                self.valor_total_diario += self.agendamento.convenio.valor_padrao
            else:
                self.valor_total_diario = self.agendamento.convenio.valor_padrao

            if self.data_atendimento == hoje.month:
                self.valor_total_mensal += self.agendamento.convenio.valor_padrao
            else:
                self.valor_total_mensal = self.agendamento.convenio.valor_padrao
            
            if self.data_atendimento == hoje.year:
                self.valor_total_anual += self.agendamento.convenio.valor_padrao
            else:
                self.valor_total_anual = self.agendamento.convenio.valor_padrao
                
        super().save(*args, **kwargs)      

    












    
    



