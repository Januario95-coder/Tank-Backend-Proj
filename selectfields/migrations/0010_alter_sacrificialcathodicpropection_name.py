# Generated by Django 3.2 on 2021-05-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectfields', '0009_alter_impresscathodicprotection_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sacrificialcathodicpropection',
            name='name',
            field=models.CharField(choices=[('Sacrificial CP available and operating - Score=0', 'Sacrificial CP available and operating'), ('Sacrificial CP not available and not operating - Score=2', 'Sacrificial CP not available and not operating')], default='Sacrificial CP available and operating - Score=0', max_length=100, verbose_name='1: Impressed cathodic protection'),
        ),
    ]
