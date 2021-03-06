# Generated by Django 3.0.8 on 2020-07-30 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalfinancialinstitute',
            name='additionalContactPersonEmail',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='internationalfinancialinstitute',
            name='additionalContactPersonFullname',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='internationalfinancialinstitute',
            name='additionalContactPersonPhoneNumber',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='internationalfinancialinstitute',
            name='additionalContactPersonPosition',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='internationalfinancialinstitute',
            name='responsiblePersonEmail',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='internationalfinancialinstitute',
            name='responsiblePersonFullname',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='internationalfinancialinstitute',
            name='responsiblePersonPhoneNumber',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='internationalfinancialinstitute',
            name='responsiblePersonPosition',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
