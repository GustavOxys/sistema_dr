# Generated by Django 4.2.5 on 2024-03-07 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0047_atendimento_editado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data_hora_agendamento',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 13, 5, 6, 440119, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='data_hora_atendimento',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 16, 5, 6, 440119, tzinfo=datetime.timezone.utc)),
        ),
    ]
