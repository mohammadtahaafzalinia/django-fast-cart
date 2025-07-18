# Generated by Django 4.2.3 on 2024-01-24 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products_module', '0033_alter_product_code_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code_product',
            field=models.CharField(default='kyX_583LcY', max_length=11, unique=True, verbose_name='کد محصول'),
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_module.product', verbose_name='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
        ),
    ]
