# Generated by Django 3.1.5 on 2021-01-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0006_remove_image_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='if_main',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
