# Generated by Django 4.0.5 on 2023-02-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]