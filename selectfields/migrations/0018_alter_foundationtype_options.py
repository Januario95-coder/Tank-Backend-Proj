# Generated by Django 3.2 on 2021-05-13 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selectfields', '0017_alter_foundationtype_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foundationtype',
            options={'ordering': ['id'], 'verbose_name': 'Foundation Type', 'verbose_name_plural': 'Foundation Type'},
        ),
    ]
