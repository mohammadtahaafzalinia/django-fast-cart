# Generated by Django 4.2.3 on 2024-01-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_module', '0040_alter_product_code_product'),
        ('user_module', '0008_user_favorites_delete_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(related_name='Favorites', to='products_module.product', verbose_name='علاقه مندی ها'),
        ),
    ]
