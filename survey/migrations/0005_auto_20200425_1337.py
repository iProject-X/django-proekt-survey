# Generated by Django 3.0.5 on 2020-04-25 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20200425_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otvet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Profil'),
        ),
    ]