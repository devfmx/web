# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0004_press'),
    ]

    operations = [
        migrations.RenameField(
            model_name='press',
            old_name='press_namme',
            new_name='press_name',
        ),
    ]
