# Generated by Django 4.2.10 on 2024-03-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0010_tradingaccount_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='reason',
            field=models.CharField(choices=[('TP', 'TP'), ('SL', 'TP')], default='TP', max_length=2),
        ),
    ]