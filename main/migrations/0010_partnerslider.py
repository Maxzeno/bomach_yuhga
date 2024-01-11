# Generated by Django 4.2.2 on 2023-06-20 09:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_service_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='N/A', max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
