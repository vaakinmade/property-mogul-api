# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20171119_2302'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ListingImage',
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
