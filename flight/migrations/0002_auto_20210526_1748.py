# Generated by Django 3.1.5 on 2021-05-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0011_auto_20210526_0949'),
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepFlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_type', models.CharField(blank=True, choices=[('B737', 'B737'), ('B747', 'B747'), ('A330', 'A330'), ('B777', 'B777')], max_length=10, null=True)),
                ('f_number', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('f_registration', models.CharField(blank=True, default='', max_length=5, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Flight',
            new_name='ArrFlight',
        ),
    ]