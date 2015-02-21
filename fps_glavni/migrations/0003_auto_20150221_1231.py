# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fps_glavni', '0002_auto_20150221_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='code',
        ),
        migrations.AlterField(
            model_name='politicalparty',
            name='slug',
            field=models.SlugField(unique=True, max_length=200, verbose_name='slug'),
            preserve_default=True,
        ),
    ]
