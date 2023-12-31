# Generated by Django 4.2.4 on 2023-09-06 16:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auction_watchlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bid_auction',
            new_name='auction',
        ),
        migrations.AddField(
            model_name='auction',
            name='date_start',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction',
            name='date_end',
            field=models.DateField(verbose_name=datetime.datetime(2023, 9, 13, 19, 13, 31, 888940)),
        ),
    ]
