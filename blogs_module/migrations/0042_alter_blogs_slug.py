# Generated by Django 4.2.3 on 2024-01-26 09:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_module', '0041_alter_blogs_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('f67bad6c-8876-490f-b848-59b77fe54567'), null=True, unique=True, verbose_name='اسلاگ'),
        ),
    ]
