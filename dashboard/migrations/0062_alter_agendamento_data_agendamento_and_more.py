# Generated by Django 5.0.3 on 2024-04-25 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0061_procedimento_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data_agendamento',
            field=models.DateTimeField(default=datetime.date(2024, 4, 25)),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_hora_agendamento',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 15, 15, 43, 845683, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='data_hora_atendimento',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 18, 15, 43, 845683, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='bairro',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cep',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cidade',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='endereco',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estado',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nome_mae',
            field=models.CharField(blank=True, default='', max_length=55),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rg',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
