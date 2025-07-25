# Generated by Django 4.2.3 on 2024-03-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0005_homesettings_icon_phone'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='homesettings',
            name='max_items_limit1',
        ),
        migrations.RemoveConstraint(
            model_name='sitesettings',
            name='max_items_limit3',
        ),
        migrations.AddConstraint(
            model_name='homesettings',
            constraint=models.CheckConstraint(check=models.Q(('id__lt', 2)), name='max_items_limit1'),
        ),
        migrations.AddConstraint(
            model_name='sitesettings',
            constraint=models.CheckConstraint(check=models.Q(('id__lt', 3)), name='max_items_limit3'),
        ),
    ]
