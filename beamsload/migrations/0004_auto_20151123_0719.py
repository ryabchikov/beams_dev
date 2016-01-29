# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beamsload', '0003_auto_20151120_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='beams',
            new_name='beam',
        ),
    ]
