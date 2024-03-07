# Generated by Django 4.2.5 on 2024-03-05 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0043_alter_agendamento_data_agendamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data_agendamento',
            field=models.DateTimeField(default=datetime.date(2024, 3, 5)),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_hora_agendamento',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 5, 13, 5, 38, 594777, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='data_hora_atendimento',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 5, 16, 5, 38, 595776, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='imc',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
