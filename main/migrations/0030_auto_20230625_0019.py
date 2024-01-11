# Generated by Django 3.2.18 on 2023-06-24 23:19

from django.db import migrations, models
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_productimage_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(default=main.models.product_id, max_length=6, primary_key=True, serialize=False),
        ),
    ]