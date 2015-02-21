# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fps_glavni', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='politicalparty',
            name='slug',
            field=models.SlugField(default='', max_length=200, verbose_name='slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amount',
            name='amount',
            field=models.DecimalField(default=0, verbose_name='Iznos', max_digits=20, decimal_places=2),
            preserve_default=True,
        ),
    ]
