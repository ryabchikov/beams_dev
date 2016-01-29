# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beamsload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beams',
            name='satellite_name',
            field=models.CharField(max_length=30, default='None'),
        ),
    ]
