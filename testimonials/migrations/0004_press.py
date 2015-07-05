# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0003_auto_20150705_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quoute', models.CharField(max_length=255, null=True, blank=True)),
                ('press_namme', models.CharField(max_length=255, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'press', blank=True)),
                ('link', models.URLField(null=True, blank=True)),
            ],
        ),
    ]
