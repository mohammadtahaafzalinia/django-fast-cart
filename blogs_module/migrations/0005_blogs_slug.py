# Generated by Django 4.2.3 on 2023-12-18 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_module', '0004_blogs_list_page_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name=''),
        ),
    ]
