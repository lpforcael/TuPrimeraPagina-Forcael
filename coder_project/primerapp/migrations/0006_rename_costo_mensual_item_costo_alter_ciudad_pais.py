# Generated by Django 4.2.7 on 2023-12-20 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerapp', '0005_remove_item_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='costo_mensual',
            new_name='costo',
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='pais',
            field=models.CharField(max_length=50),
        ),
    ]
