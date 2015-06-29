# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensei',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('specialty', models.CharField(max_length=600)),
                ('short_description', models.CharField(max_length=600, null=True, blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'senseis', blank=True)),
            ],
        ),
    ]
