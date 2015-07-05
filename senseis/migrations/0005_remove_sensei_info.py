# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('senseis', '0004_auto_20150705_0720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensei',
            name='info',
        ),
    ]
