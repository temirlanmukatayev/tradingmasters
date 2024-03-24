# Generated by Django 4.2.11 on 2024-03-24 08:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trades', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tradingaccount',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tradelink',
            name='trade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trades.trade'),
        ),
        migrations.AddField(
            model_name='trade',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trade',
            name='trading_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trades.tradingaccount'),
        ),
        migrations.AddIndex(
            model_name='tradingaccount',
            index=models.Index(fields=['-title'], name='trades_trad_title_bc6c7a_idx'),
        ),
    ]