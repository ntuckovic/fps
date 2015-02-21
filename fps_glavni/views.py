# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.db.models import Sum
from django.views.generic import TemplateView
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import PoliticalParty, Amount
from datetime import datetime

from django.shortcuts import get_object_or_404
import settings

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context["projekt"] = settings.PROJECT_NAME 
        context["desc"] = settings.PROJECT_DESCRIPTION
        context["ctx"] = u"Početna"

        year = 2012 # datetime.now().year
        parties = PoliticalParty.objects.filter(amounts__year=year).annotate(total=Sum('amounts__amount'))

        context['parties'] = parties

        return context


class PartyView(TemplateView):
    template_name = "party.html"


    def dispatch(self, request, *args, **kwargs):
        self.party_slug = kwargs.get('slug', None)
        return super(PartyView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PartyView, self).get_context_data()
        party = get_object_or_404(PoliticalParty, slug=self.party_slug)
        amounts = party.amounts.select_related('income')
        context['party'] = party
        years = set(amounts.values_list('year', flat=True))
        pies = []
        total = []
        for year in years:
            total.append( (year, amounts.filter(year=year).aggregate(Sum('amount')) ) )
            pies.append((year, amounts.filter(year=year)))
        context['total'] = total
        context['pies'] = pies

        return context

class ImpressumView(TemplateView):
    template_name = "impressum.html"
