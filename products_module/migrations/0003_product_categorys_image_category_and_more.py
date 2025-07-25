# Generated by Django 4.2.3 on 2023-12-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_module', '0002_product_short_description_alter_product_code_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_categorys',
            name='image_category',
            field=models.ImageField(blank=True, null=True, upload_to='Product_category/%Y', verbose_name='عکس دسته بندی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code_product',
            field=models.CharField(default='V6bBFLPl9F', max_length=11, unique=True, verbose_name='کد محصول'),
        ),
    ]
