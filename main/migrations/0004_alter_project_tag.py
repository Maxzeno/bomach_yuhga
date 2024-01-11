# Generated by Django 4.2.2 on 2023-06-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_project_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tag',
            field=models.CharField(choices=[('REAL-ESTATE-SERVICE', 'REAL ESTATE SERVICES'), ('LAND-SERVICES', 'LAND SERVICES'), ('ENGINEERING-CONSTRUCTION', 'ENGINEERING / CONSTRUCTION'), ('WEB-DEVELOPMENT-BUSINESS-AUTOMATION', 'WEB DEVELOPMENT / BUSINESS AUTOMATION'), ('LOGISTICS-SERVICES', 'LOGISTICS SERVICES'), ('FOOD-AND-FARM', 'FOOD AND FARM')], max_length=255),
        ),
    ]
