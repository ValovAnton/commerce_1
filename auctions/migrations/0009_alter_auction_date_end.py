# Generated by Django 4.2.4 on 2023-09-07 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_auction_date_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='date_end',
            field=models.DateField(default=datetime.date(2023, 9, 14), verbose_name='Auction ends at'),
        ),
    ]
