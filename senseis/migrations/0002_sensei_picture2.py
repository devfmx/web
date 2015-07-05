# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('senseis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensei',
            name='picture2',
            field=models.ImageField(null=True, upload_to=b'senseis', blank=True),
        ),
    ]
