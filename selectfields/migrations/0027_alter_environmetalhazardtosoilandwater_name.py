# Generated by Django 3.2 on 2021-05-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectfields', '0026_auto_20210513_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environmetalhazardtosoilandwater',
            name='name',
            field=models.CharField(choices=[('No or negligle environment effect - Score=1', 'No or negligle environment effect'), ('Environmental nuisance affecting neighbourhood - Score=2', 'Environmental nuisance affecting neighbourhood'), ('Environmental pollution, Extensive restoration required - Score=3', 'Environmental pollution, Extensive restoration required'), ('Severe damage/nuisance/pollution over large area- Score=4', 'Severe damage/nuisance/pollution over large area')], default='Nor or negligle environment effect - Score=1', max_length=100, verbose_name='14a: Environmetal hazard to soil and water as the potential to cause'),
        ),
    ]
