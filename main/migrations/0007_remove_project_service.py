# Generated by Django 4.2.2 on 2023-06-20 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_customerreview_employee_homeslider_service_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='service',
        ),
    ]
