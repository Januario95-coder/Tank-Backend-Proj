# Generated by Django 3.1.7 on 2021-04-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell_plates', '0006_remove_consequencefactordata_continued_location_of_tank_farm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consequencefactordata',
            name='likelihood_of_injury_to_personnel',
            field=models.CharField(choices=[('No injury or near miss - score=1', 'No injury or near miss'), ('Minor injury - score=2', 'Minor injury'), ('Lost time injury/Medical treatment - score=3', 'Lost time injury/Medical treatment'), ('Serious injury/fatality on site - score=4', 'Serious injury/fatality on site')], max_length=100, verbose_name='9a: Likelihood of injury to personnel'),
        ),
        migrations.AlterField(
            model_name='consequencefactordata',
            name='location_of_tank_farm',
            field=models.CharField(choices=[('Tank farm within an abandonned area - score=1', 'Tank farm within an abandonned area'), ('Flat tank farm - score=2', 'Flat tank farm'), ('Flopping tank farm - score=3', 'Flopping tank farm'), ('In plant area within populous area - score=4', 'In plant area within populous area')], max_length=100, verbose_name='9d: Location of tank farm'),
        ),
        migrations.AlterField(
            model_name='consequencefactordata',
            name='product_flammability_as_per_MCSP',
            field=models.CharField(choices=[('Class III(1) and unclassified product - score=1', 'Class III(1) and unclassified product'), ('Class II(1) product - score=2', 'Class II(1) product'), ('Class II(2) and III(2) product - score=3', 'Class II(2) and III(2) product'), ('Class I product - score=4', 'Class I product')], max_length=100, verbose_name='9b: Product flammability as per MCSP'),
        ),
        migrations.AlterField(
            model_name='consequencefactordata',
            name='product_toxicity',
            field=models.CharField(choices=[('Non-toxic substances - score=1', 'Non-toxic substances'), ('Toxic substance if in contact with other substances - score=2', 'Toxic substance if in contact with other substances'), ('Toxic substance - score=3', 'Toxic substance'), ('Extremely toxic substance - score=4', 'Extremely toxic substance')], max_length=100, verbose_name='9c: Product toxicity'),
        ),
    ]
