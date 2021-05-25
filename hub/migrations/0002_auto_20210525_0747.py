# Generated by Django 3.1.5 on 2021-05-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_shipment_type', models.CharField(default='TTSP', max_length=55)),
                ('str_hndl_temp', models.CharField(choices=[('COL', 'COL'), ('CRT', 'CRT'), ('ERT', 'ERT'), ('NFR', 'NFR')], default='COL', max_length=10)),
                ('str_awb_owner', models.CharField(default='001', max_length=3)),
                ('str_awb_number', models.CharField(default='00000001', max_length=11)),
                ('awb_pcs', models.IntegerField(blank=True, null=True)),
                ('awb_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('awb_vol', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='StateRequest',
        ),
    ]
