# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'testimonials', blank=True),
        ),
    ]
