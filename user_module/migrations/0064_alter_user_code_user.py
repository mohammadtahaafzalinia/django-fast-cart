# Generated by Django 4.2.3 on 2024-03-26 12:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0063_alter_user_code_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code_user',
            field=models.CharField(default=[uuid.UUID('e6201105-1928-4569-8ee8-9399c5fbfb6b')], max_length=20, verbose_name='کد کاربر'),
        ),
    ]
