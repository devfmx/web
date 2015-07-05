# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testimonial', models.TextField(max_length=1000)),
                ('person', models.CharField(max_length=255)),
                ('person_title', models.CharField(max_length=255)),
            ],
        ),
    ]
