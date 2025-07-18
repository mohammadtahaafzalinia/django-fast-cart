# Generated by Django 4.2.3 on 2024-01-19 17:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_module', '0031_alter_blogs_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('7f7c7f0a-acf8-4527-b41e-e36962acb172'), null=True, unique=True, verbose_name='اسلاگ'),
        ),
    ]
