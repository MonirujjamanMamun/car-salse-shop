# Generated by Django 4.2.7 on 2023-12-26 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brandmodel',
            name='car',
        ),
    ]
