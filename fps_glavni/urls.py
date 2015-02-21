# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from views import IndexView

urlpatterns = patterns('',
    (r'^', IndexView.as_view()),
)
