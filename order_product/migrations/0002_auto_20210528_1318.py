# Generated by Django 3.2.3 on 2021-05-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_varition_is_active'),
        ('order_product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='color',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='size',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variation',
            field=models.ManyToManyField(blank=True, to='store.Varition'),
        ),
    ]
