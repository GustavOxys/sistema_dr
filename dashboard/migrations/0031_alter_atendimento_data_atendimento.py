# Generated by Django 4.2.5 on 2024-02-02 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_alter_atendimento_data_atendimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='data_atendimento',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 2, 19, 11, 24, 141356, tzinfo=datetime.timezone.utc)),
        ),
    ]
