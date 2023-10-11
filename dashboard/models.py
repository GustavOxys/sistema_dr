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
    convenio = models.ForeignKey(Convenio, on_delete=models.SET_NULL, blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_consulta = models.DateTimeField()
    observacao = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nome   