# Generated by Django 4.2.3 on 2024-03-21 13:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0040_alter_user_code_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code_user',
            field=models.CharField(default=[uuid.UUID('3dc5eff2-de59-453f-a625-07c8233e0925')], max_length=20, verbose_name='کد کاربر'),
        ),
    ]
