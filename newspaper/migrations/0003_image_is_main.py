# Generated by Django 3.1.5 on 2021-01-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_auto_20210115_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
