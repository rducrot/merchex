# Generated by Django 4.1.3 on 2022-11-14 10:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('RE', 'Records'), ('CL', 'Clothing'), ('PO', 'Posters'), ('MI', 'Miscellaneous')], default='MI', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)]),
        ),
        migrations.AlterField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)]),
        ),
    ]
