# Generated by Django 3.1.5 on 2021-05-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StateRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inbnd_flit_date', models.DateField(blank=True, null=True)),
                ('inbnd_flit_nmb', models.CharField(default='', max_length=6, null=True)),
                ('outbnd_flit_nmb', models.CharField(default='', max_length=6, null=True)),
                ('outbnd_flit_date', models.DateField(blank=True, null=True)),
                ('str_shipment_type', models.CharField(default='TTSP', max_length=55)),
                ('str_hndl_temp', models.CharField(choices=[('COL', 'COL'), ('CRT', 'CRT'), ('ERT', 'ERT'), ('NFR', 'NFR')], default='COL', max_length=10)),
                ('str_awb', models.CharField(default='58000000001', max_length=11)),
                ('state_status', models.CharField(choices=[('NW', 'NEW'), ('OTF', 'OKTOFWD'), ('RCD', 'REJECTED'), ('CCD', 'CANCELED')], default='NEW', max_length=36)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]