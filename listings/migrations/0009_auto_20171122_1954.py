# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20171122_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingimage',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listingimages', to='listings.Listing'),
        ),
    ]
