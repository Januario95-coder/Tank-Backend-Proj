# Generated by Django 3.2 on 2021-05-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectfields', '0012_alter_bottomplatesinternalcoatinglining_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottomplatesexternalcoating',
            name='name',
            field=models.CharField(choices=[('External coating applied and quality is sound - Score=0', 'External coating applied and quality is sound'), ('External coating applied but quality is poor - Score=1', 'External coating applied but quality is poor'), ('No coating is applied - Score=2', 'No coating is applied')], default='Internal coating applied and quality is sound - Score=0', max_length=100, verbose_name='4: Bottom plates internal coating (other than shop primer)'),
        ),
    ]