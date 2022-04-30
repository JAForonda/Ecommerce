# Generated by Django 3.2.12 on 2022-04-09 00:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='None', max_length=400),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 0, 35, 18, 660510, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='None', max_length=300),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='updatd_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 0, 35, 18, 660546, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.CharField(default='None', max_length=200),
        ),
    ]