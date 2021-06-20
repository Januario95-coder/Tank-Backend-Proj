# Generated by Django 3.2 on 2021-05-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectfields', '0033_evidenceavailableofcompletingpdca'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evidenceavailableofcompletingpdca',
            options={'verbose_name': 'Is Evidence Available Of Completing PDCA Cycle On Inspection Activities', 'verbose_name_plural': 'Is Evidence Available Of Completing PDCA Cycle On Inspection Activities'},
        ),
        migrations.AlterField(
            model_name='evidenceavailableofcompletingpdca',
            name='name',
            field=models.CharField(choices=[('Yes - Score=1', 'Yes'), ('No - Score=0', 'No')], default='No - Score=0', max_length=100, verbose_name='Is Evidence Available Of Completing PDCA Cycle On Inspection Activities?'),
        ),
    ]
