# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localbusiness', '0003_localbusiness_site_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='localbusiness',
            name='postalCode',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='localbusiness',
            name='name',
            field=models.CharField(default='Unisport A/S', max_length=100),
        ),
    ]
