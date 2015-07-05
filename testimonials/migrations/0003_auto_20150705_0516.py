# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_testimonial_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'senseis', blank=True),
        ),
    ]
