# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_auto_20150704_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'program_images'),
        ),
    ]
