# Generated by Django 4.2.3 on 2023-12-23 13:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_module', '0009_alter_blogs_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='توزیحات')),
            ],
        ),
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('867c329c-9125-4373-9ad9-ca8504737e5d'), null=True, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='more_detail',
            field=models.ManyToManyField(to='blogs_module.moredetail', verbose_name='توزیحات بیشتر'),
        ),
    ]
