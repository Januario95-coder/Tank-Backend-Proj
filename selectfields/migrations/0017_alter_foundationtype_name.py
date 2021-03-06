# Generated by Django 3.2 on 2021-05-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectfields', '0016_alter_productcorrosivity_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foundationtype',
            name='name',
            field=models.CharField(choices=[('Traditional granular soil / sand type - Score=2', 'Traditional granular soil / sand type'), ('Sand pad with annular ring of coarse granular material - Score=1.33', 'Sand pad with annular ring of coarse granular material'), ('Sand pad with annular ring of coarse granular material and with sound sand/bitumen top layer - Score=0.67', 'Sand pad with annular ring of coarse granular material and with sound sand/bitumen top layer'), ('Concrete raft under tank - Score=0', 'Concrete raft under tank'), ('Piled concrete raft - Score=0', 'Piled concrete raft')], default='Piled concrete raft - Score=0', max_length=330, verbose_name='7: Foundation type'),
        ),
    ]
