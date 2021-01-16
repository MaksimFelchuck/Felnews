# Generated by Django 3.1.5 on 2021-01-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(blank=True, default=None, max_length=50)),
                ('text', models.TextField(blank=True, default=None)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='static/images')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]