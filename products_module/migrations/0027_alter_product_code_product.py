# Generated by Django 4.2.3 on 2024-01-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_module', '0026_alter_product_code_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code_product',
            field=models.CharField(default='7p8Bp1Ageg', max_length=11, unique=True, verbose_name='کد محصول'),
        ),
    ]
