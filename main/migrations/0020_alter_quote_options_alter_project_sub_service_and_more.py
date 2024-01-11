# Generated by Django 4.2.2 on 2023-06-21 16:41

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_quote_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'verbose_name': 'Service Quote', 'verbose_name_plural': 'Service Quote'},
        ),
        migrations.AlterField(
            model_name='project',
            name='sub_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subservice'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('priority', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.service')),
            ],
            bases=(models.Model, main.models.ImageUrl),
        ),
    ]