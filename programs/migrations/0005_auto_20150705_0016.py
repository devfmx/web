# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_auto_20150704_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='actual_price',
            field=models.CharField(default=b'', max_length=60),
        ),
        migrations.AlterField(
            model_name='program',
            name='old_price',
            field=models.CharField(default=b'', max_length=60),
        ),
    ]
