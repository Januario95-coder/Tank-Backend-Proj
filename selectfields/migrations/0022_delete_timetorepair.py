# Generated by Django 3.2 on 2021-05-13 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bottom_plates', '0003_remove_consequencefactordata_time_to_repair'),
        ('selectfields', '0021_alter_timetorepair_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TimeToRepair',
        ),
    ]