# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from views import IndexView, PartyView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name="fps_index"),
    url(r'stranka/(?P<slug>\w+)$', PartyView.as_view(), name="fps_party"),
)
