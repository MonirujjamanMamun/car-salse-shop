# Generated by Django 4.2.7 on 2023-12-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
