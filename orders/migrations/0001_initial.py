# Generated by Django 3.2.3 on 2021-05-24 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=55)),
                ('first_name', models.CharField(max_length=155)),
                ('last_name', models.CharField(max_length=155)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=155)),
                ('address_line_1', models.CharField(max_length=155)),
                ('address_line_2', models.CharField(blank=True, max_length=155)),
                ('country', models.CharField(max_length=155)),
                ('state', models.CharField(max_length=155)),
                ('city', models.CharField(max_length=155)),
                ('order_note', models.CharField(blank=True, max_length=355)),
                ('order_total', models.FloatField()),
                ('tax', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=155)),
                ('ip', models.CharField(blank=True, max_length=25)),
                ('is_ordered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.payment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
