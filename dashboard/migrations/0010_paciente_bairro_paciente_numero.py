# Generated by Django 4.2.5 on 2023-10-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_paciente_data_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='bairro',
            field=models.CharField(blank=True, default='Desconhecido', max_length=20),
        ),
        migrations.AddField(
            model_name='paciente',
            name='numero',
            field=models.CharField(blank=True, default='Desconhecido', max_length=20),
        ),
    ]