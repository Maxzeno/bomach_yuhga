# Generated by Django 3.2.18 on 2023-06-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20230627_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='location',
            field=models.CharField(choices=[('Enugu Branch', 'Enugu Branch'), ('Port Harcourt Branch', 'Port Harcourt Branch')], default='Enugu Branch', max_length=1000),
        ),
    ]
