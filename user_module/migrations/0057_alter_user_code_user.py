# Generated by Django 4.2.3 on 2024-03-25 19:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0056_alter_user_code_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code_user',
            field=models.CharField(default=[uuid.UUID('8007c056-26b2-4cef-bcbd-2d0936dc9426')], max_length=20, verbose_name='کد کاربر'),
        ),
    ]
