# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_program_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='actual_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='program',
            name='old_price',
            field=models.IntegerField(default=0),
        ),
    ]
