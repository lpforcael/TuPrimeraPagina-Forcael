# Generated by Django 4.2.7 on 2023-12-15 03:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('primerapp', '0003_item_ciudad_alter_item_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]