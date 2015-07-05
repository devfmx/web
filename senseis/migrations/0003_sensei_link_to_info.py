# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('senseis', '0002_sensei_picture2'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensei',
            name='link_to_info',
            field=models.URLField(default=True, max_length=255),
        ),
    ]
