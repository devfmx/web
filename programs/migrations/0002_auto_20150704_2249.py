# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='actual_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='program',
            name='old_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='program',
            name='requirements',
            field=models.TextField(default=b'', null=True),
        ),
    ]
