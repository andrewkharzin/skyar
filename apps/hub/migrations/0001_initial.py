# Generated by Django 3.2.3 on 2021-05-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_shipment_type', models.CharField(default='TTSP', max_length=55)),
                ('str_awb_owner', models.CharField(default='001', max_length=3)),
                ('str_awb_number', models.CharField(default='00000001', max_length=11)),
                ('awb_pcs', models.IntegerField(blank=True, null=True)),
                ('awb_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('awb_vol', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('origin', models.CharField(default='XXX', max_length=3)),
                ('destination', models.CharField(default='XXX', max_length=3)),
                ('shc_code1', models.CharField(blank=True, choices=[('ICE', 'ICE'), ('MAG', 'MAG'), ('ELI', 'ELI'), ('COL', 'COL'), ('ERT', 'ERT'), ('CRT', 'CRT'), ('NFR', 'NFR'), ('ACT', 'ACT')], default='', max_length=3, null=True)),
                ('shc_code2', models.CharField(blank=True, choices=[('ICE', 'ICE'), ('MAG', 'MAG'), ('ELI', 'ELI'), ('COL', 'COL'), ('ERT', 'ERT'), ('CRT', 'CRT'), ('NFR', 'NFR'), ('ACT', 'ACT')], default='', max_length=3, null=True)),
                ('shc_code3', models.CharField(blank=True, choices=[('ICE', 'ICE'), ('MAG', 'MAG'), ('ELI', 'ELI'), ('COL', 'COL'), ('ERT', 'ERT'), ('CRT', 'CRT'), ('NFR', 'NFR'), ('ACT', 'ACT')], default='', max_length=3, null=True)),
                ('shc_code4', models.CharField(blank=True, choices=[('ICE', 'ICE'), ('MAG', 'MAG'), ('ELI', 'ELI'), ('COL', 'COL'), ('ERT', 'ERT'), ('CRT', 'CRT'), ('NFR', 'NFR'), ('ACT', 'ACT')], default='', max_length=3, null=True)),
                ('shc_code5', models.CharField(blank=True, choices=[('ICE', 'ICE'), ('MAG', 'MAG'), ('ELI', 'ELI'), ('COL', 'COL'), ('ERT', 'ERT'), ('CRT', 'CRT'), ('NFR', 'NFR'), ('ACT', 'ACT')], default='', max_length=3, null=True)),
                ('handling', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
