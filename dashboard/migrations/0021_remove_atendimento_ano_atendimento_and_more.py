# Generated by Django 4.2.5 on 2024-01-15 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_atendimento_ano_atendimento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimento',
            name='ano_atendimento',
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='mes_atendimento',
        ),
        migrations.AddField(
            model_name='atendimento',
            name='total_anual',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='total_diario',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='total_mensal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='data_atendimento',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 14, 54, 33, 678310, tzinfo=datetime.timezone.utc)),
        ),
    ]