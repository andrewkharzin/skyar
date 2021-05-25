# Generated by Django 3.1.5 on 2021-05-25 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_auto_20210525_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='awb_vol',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='awb_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
