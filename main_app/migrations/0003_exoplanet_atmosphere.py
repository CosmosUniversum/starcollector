# Generated by Django 3.2.7 on 2022-01-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_exoplanet'),
    ]

    operations = [
        migrations.AddField(
            model_name='exoplanet',
            name='atmosphere',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=False,
        ),
    ]
