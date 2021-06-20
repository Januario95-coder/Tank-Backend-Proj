# Generated by Django 3.2 on 2021-05-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectfields', '0038_doestheitemevaluationhavesignificantpitting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doestheitemevaluationhavesignificantpitting',
            name='name',
            field=models.CharField(choices=[('Yes - Score=0', 'Yes'), ('No - Score=1', 'No')], default='No - Score=1', max_length=100, verbose_name='Does the Item Evaluation Have Significant Pitting?'),
        ),
    ]