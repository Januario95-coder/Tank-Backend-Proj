# Generated by Django 3.2 on 2021-05-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectfields', '0042_delete_typeofinterconnectingbottomplatewelds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='istheconstructionsuchthatcorrosionmaybereducedbythechosenweldconfiguration',
            name='name',
            field=models.CharField(choices=[('Annual plates butt welded with backing strip - Score=1.0', 'Annual plates butt welded with backing strip'), ('Annular plates butt welded from both sides - Score=0.75', 'Annular plates butt welded from both sides'), ('No annular section, but double pass lap welded sketch plates - Score=-0.50', 'No annular section, but double pass lap welded sketch plates'), ('No annular section but single pass lap welds sketch plates - Score=0.25', 'No annular section but single pass lap welds sketch plates')], default='No - Score=1', max_length=100, verbose_name='Is the Construction such that Corrosion may be Reduced by the Chosen Weld Configuration?'),
        ),
    ]
