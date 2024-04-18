# Generated by Django 4.2.5 on 2024-03-14 13:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0053_convenio_n_reconsultas_convenio_prazo_reconsultas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='convenio',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_agendamento',
            field=models.DateTimeField(default=datetime.date(2024, 3, 14)),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_hora_agendamento',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 10, 12, 21, 506220, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='data_hora_atendimento',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 13, 12, 21, 506220, tzinfo=datetime.timezone.utc)),
        ),
    ]