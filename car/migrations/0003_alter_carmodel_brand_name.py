# Generated by Django 4.2.7 on 2023-12-26 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_remove_brandmodel_car'),
        ('car', '0002_carmodel_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brandmodel'),
        ),
    ]
