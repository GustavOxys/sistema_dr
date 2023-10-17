from django.contrib import admin
from dashboard import models


@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'show',
    list_display_links = 'id', 'nome',
    list_editable = 'show',


@admin.register(models.Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome',


@admin.register(models.Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome',
    



