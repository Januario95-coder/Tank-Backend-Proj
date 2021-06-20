# Generated by Django 3.2 on 2021-05-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectfields', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreProceduresInPlaceToPreventWaterContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Yes - Score=1', 'Yes'), ('No', 'No - Score=0')], default='Yes - Score=1', max_length=350, verbose_name='Are Procedures In Place To Prevent Water Contact')),
            ],
        ),
        migrations.CreateModel(
            name='IsTheCorrosionRateDeterminedWithAtLeast2Sources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Yes - Score=1', 'Yes'), ('No', 'No - Score=0')], default='Yes - Score=1', max_length=350, verbose_name='Is The Corrosion Rate Determined With At Least 2 Sources')),
            ],
        ),
        migrations.CreateModel(
            name='IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Yes - Score=1', 'Yes'), ('No', 'No - Score=0')], default='Yes - Score=1', max_length=350, verbose_name='Is The Degradation Speed Calculated By Using At Least 3 Measurement Points')),
            ],
        ),
        migrations.CreateModel(
            name='WhichMethodIsUsed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('LS fit - Score=0.6', 'LS fit'), ('Last 2 Points - Score=0.5', 'Last 2 Points'), ('Literature - Score=0', 'Literature'), ('Similar Service - Score=1', 'Similar Service'), ('2 Methods Used - Score=1', '2 Methods Used')], default='Yes - Score=1', max_length=350, verbose_name='Which Method Is Used')),
            ],
        ),
        migrations.AlterField(
            model_name='accelerationfactorforpitting',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bottomplatesexternalcoating',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bottomplatesinternalcoatinglining',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='costofrepair',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='effectivenessofdrainage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='environmetalhazardtosoilandwater',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='foundationtype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='frequencyofinternalinspections',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='heatingcoilsintank',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='heightoffoundation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='impresscathodicprotection',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='likelihoodofinjurytopersonnel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='locationoftankfarm',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ndtmethodusedforthicknessmeasurements',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ndtmethodusedforthicknessmeasurements',
            name='name',
            field=models.CharField(choices=[('Floor scan + US - Score=+0.1', 'Floor scan + US'), ('US on gridline system - Score=0', 'US on gridline system'), ('Visual + Spot ultrasonic (US) - Score=-0.1)', 'Visual + Spot ultrasonic (US)')], default='Floor scan + US - Score=-0.1', max_length=100, verbose_name='28: NDT method used for thickness measurements'),
        ),
        migrations.AlterField(
            model_name='probablemagnitudeofproductloss',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='productcorrosivity',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='productflammabilityaspermcsp',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='producttoxicity',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sacrificialcathodicpropection',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='storageconditions',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='timetorepair',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='typeofbottom',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='typeofinterconnectingbottomplatewelds',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vapouremission',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
