# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beamsload', '0002_beams_satellite_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=14, max_digits=17)),
                ('longitude', models.DecimalField(decimal_places=14, max_digits=17)),
            ],
        ),
        migrations.RenameModel(
            old_name='Beams',
            new_name='Beam',
        ),
        migrations.RemoveField(
            model_name='points',
            name='beams',
        ),
        migrations.DeleteModel(
            name='Points',
        ),
        migrations.AddField(
            model_name='point',
            name='beams',
            field=models.ForeignKey(to='beamsload.Beam'),
        ),
    ]
