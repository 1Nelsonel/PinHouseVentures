# Generated by Django 4.0.5 on 2023-02-02 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]