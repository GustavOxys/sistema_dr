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
    nome = models.CharField(max_length=55)
    telefone = models.CharField(max_length=30)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.DO_NOTHING)
    convenio = models.ForeignKey(Convenio, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_consulta = models.DateField(default='0000-00-00')
    hora_consulta = models.TimeField(default='09:00')
    observacao = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def data_formatada(self):
        return self.data_consulta.strftime('%d/%m/%y')

    def __str__(self):
        return self.nome   