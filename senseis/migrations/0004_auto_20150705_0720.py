# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('senseis', '0003_sensei_link_to_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensei',
            name='link_to_info',
        ),
        migrations.AddField(
            model_name='sensei',
            name='info',
            field=models.URLField(default=b'#', max_length=255),
        ),
    ]
