from django.contrib import admin
from dashboard import models


@admin.register(models.Paciente)
@admin.register(models.Convenio)
@admin.register(models.Procedimento)

class PacienteAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 



