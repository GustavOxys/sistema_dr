# Generated by Django 5.0.3 on 2024-04-17 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0059_alter_agendamento_data_hora_agendamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data_agendamento',
            field=models.DateTimeField(default=datetime.date(2024, 4, 17)),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_hora_agendamento',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 17, 10, 26, 48, 287, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='data_hora_atendimento',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 17, 13, 26, 48, 1283, tzinfo=datetime.timezone.utc)),
        ),
    ]
