# Generated by Django 4.2.5 on 2023-10-31 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_atendimento_prontuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='idade',
            field=models.DecimalField(blank=True, decimal_places=2, default=18, max_digits=5),
        ),
    ]
