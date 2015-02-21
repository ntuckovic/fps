# -*- coding: utf-8 -*-
from django.db import models

class PoliticalParty(models.Model):
    name = models.CharField(verbose_name=u"Naziv stranke", max_length=200)
    short_name = models.CharField(verbose_name=u"Kratki naziv", max_length=50)

    def __unicode__(self):
        return self.short_name

    class Meta:
        verbose_name = u"Politička stranka"
        verbose_name_plural = u"Političke stranke"

class Income(models.Model):
    code = models.SmallIntegerField(verbose_name=u"Šifra")
    name = models.CharField(verbose_name=u"Naziv prihoda", max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Prihod"
        verbose_name_plural = u"Prihodi"

class Amount(models.Model):
    party = models.ForeignKey(PoliticalParty, verbose_name=u"Politička stranka")
    income = models.ForeignKey(Income, verbose_name=u"Prihod")
    amount = models.DecimalField(verbose_name=u"Iznos", decimal_places=2, max_digits=20)
    year = models.SmallIntegerField(verbose_name=u"Godina")

    def __unicode__(self):
        return self.party.short_name + ", " + self.income + ": " + str(self.amount)

    class Meta:
        verbose_name = u"Iznos"
        verbose_name_plural = u"Iznosi"

