# Generated by Django 4.2.3 on 2024-03-25 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order_success_module', '0002_alter_cartmodel_total_sum'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSuccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sum', models.PositiveIntegerField(blank=True, null=True, verbose_name='جمع نهایی')),
                ('product_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='تعداد محصولات خریداری شده')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_success_module.cartmodel', verbose_name='سبد خرید')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سبد خرید موفق',
                'verbose_name_plural': 'سبد خرید موفق',
            },
        ),
    ]
