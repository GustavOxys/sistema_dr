# Generated by Django 4.2.5 on 2024-03-12 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0049_paciente_idade_alter_agendamento_data_agendamento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=50.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_agendamento',
            field=models.DateTimeField(default=datetime.date(2024, 3, 12)),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_hora_agendamento',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 8, 28, 23, 115714, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='data_hora_atendimento',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 11, 28, 23, 116713, tzinfo=datetime.timezone.utc)),
        ),
    ]
