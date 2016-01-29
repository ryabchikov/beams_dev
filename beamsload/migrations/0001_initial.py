# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beams',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('beam_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('latitude', models.DecimalField(max_digits=17, decimal_places=14)),
                ('longitude', models.DecimalField(max_digits=17, decimal_places=14)),
                ('beams', models.ForeignKey(to='beamsload.Beams')),
            ],
        ),
    ]
