# Generated by Django 3.1.5 on 2021-05-26 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_trrequest_trr_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='trrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trrequest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='trrequest',
            name='trr_date',
            field=models.DateTimeField(blank=True, default='0000-00-00 00:00:00'),
        ),
    ]