# Generated by Django 3.2.3 on 2021-05-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=155, unique=True),
        ),
    ]
