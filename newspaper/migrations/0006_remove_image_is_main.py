# Generated by Django 3.1.5 on 2021-01-14 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0005_auto_20210115_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='is_main',
        ),
    ]
