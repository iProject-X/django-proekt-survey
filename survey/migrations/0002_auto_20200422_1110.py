# Generated by Django 3.0.5 on 2020-04-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otvet',
            name='answer',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profil',
            name='age',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='language',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profil',
            name='specialite',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stimul_slov',
            name='stimulus',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
