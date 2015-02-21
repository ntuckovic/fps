# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext, loader
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        context = {}

        context["projekt"] = "FPS - HR"
        context["desc"] = u"Prikaz financiranja političkih stranaka u RH"
        context["ctx"] = u"Početna"

        return render_to_response(self.template_name, context, context_instance=RequestContext(request, context))