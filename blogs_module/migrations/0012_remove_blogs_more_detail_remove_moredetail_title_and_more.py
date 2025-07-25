# Generated by Django 4.2.3 on 2023-12-23 14:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_module', '0011_alter_moredetail_options_moredetail_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='more_detail',
        ),
        migrations.RemoveField(
            model_name='moredetail',
            name='title',
        ),
        migrations.AddField(
            model_name='moredetail',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs_module.blogs', verbose_name='بلاگ مورد نظر'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('bd5dbfc3-0750-4470-bc90-e09b1cb1b852'), null=True, unique=True, verbose_name='اسلاگ'),
        ),
    ]
