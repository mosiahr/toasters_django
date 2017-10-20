#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import (
    ToasterListView,
    ToasterDetailView,
    hello,
)


urlpatterns = [
    url(r'^$', hello, name='hello'),
    url(r'all/', ToasterListView.as_view(), name='toasters'),
    url(r'^(?P<pk>\d+)/$$', ToasterDetailView.as_view(), name='toaster_detail'),
]