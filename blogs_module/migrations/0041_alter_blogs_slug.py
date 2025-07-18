# Generated by Django 4.2.3 on 2024-01-26 09:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_module', '0040_alter_blogs_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('2f424ca4-d861-48d9-a7e7-3060aaee1c77'), null=True, unique=True, verbose_name='اسلاگ'),
        ),
    ]
