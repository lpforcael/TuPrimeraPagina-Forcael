# Generated by Django 4.2.7 on 2023-12-23 04:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('primerapp', '0016_remove_item_actualizado_remove_item_hora_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='actualizado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]