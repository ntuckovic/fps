# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(verbose_name='Iznos', max_digits=20, decimal_places=2)),
                ('year', models.SmallIntegerField(verbose_name='Godina')),
            ],
            options={
                'verbose_name': 'Iznos',
                'verbose_name_plural': 'Iznosi',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.SmallIntegerField(verbose_name='\u0160ifra')),
                ('name', models.CharField(max_length=200, verbose_name='Naziv prihoda')),
            ],
            options={
                'verbose_name': 'Prihod',
                'verbose_name_plural': 'Prihodi',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PoliticalParty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Naziv stranke')),
                ('short_name', models.CharField(max_length=50, verbose_name='Kratki naziv')),
            ],
            options={
                'verbose_name': 'Politi\u010dka stranka',
                'verbose_name_plural': 'Politi\u010dke stranke',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='amount',
            name='income',
            field=models.ForeignKey(verbose_name='Prihod', to='fps_glavni.Income'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='amount',
            name='party',
            field=models.ForeignKey(verbose_name='Politi\u010dka stranka', to='fps_glavni.PoliticalParty'),
            preserve_default=True,
        ),
    ]
