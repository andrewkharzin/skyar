# Generated by Django 3.1.5 on 2021-05-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trrequest',
            name='trr_date',
            field=models.DateTimeField(blank=True, default=''),
        ),
    ]