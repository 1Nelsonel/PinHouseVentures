# Generated by Django 4.0.8 on 2022-12-21 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_property_delete_properties'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='airpot',
            new_name='airport',
        ),
    ]
