# Generated by Django 4.2.5 on 2024-03-12 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0050_atendimento_valor_alter_agendamento_data_agendamento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimento',
            name='valor',
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_hora_agendamento',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 8, 41, 28, 185819, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='data_hora_atendimento',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 11, 41, 28, 186844, tzinfo=datetime.timezone.utc)),
        ),
    ]