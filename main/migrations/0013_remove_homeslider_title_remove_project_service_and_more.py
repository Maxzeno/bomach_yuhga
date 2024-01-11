# Generated by Django 4.2.2 on 2023-06-21 08:39

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeslider',
            name='title',
        ),
        migrations.RemoveField(
            model_name='project',
            name='service',
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('slug', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
                ('content', ckeditor.fields.RichTextField()),
                ('rating', models.IntegerField(default=80, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be less than 0.'), django.core.validators.MaxValueValidator(100, message='Value cannot be greater than 100.')])),
                ('priority', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.service')),
            ],
            bases=(models.Model, main.models.ImageUrl),
        ),
        migrations.AddField(
            model_name='project',
            name='sub_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subservice'),
        ),
    ]
