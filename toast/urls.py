#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import (
    ToasterListView,
    ToasterDetailView,
    TagListView,
    TagDetailView,
    hello,
)


urlpatterns = [
    url(r'^$', hello, name='hello'),
    url(r'all/', ToasterListView.as_view(), name='toasters'),
    url(r'^(?P<pk>\d+)/$', ToasterDetailView.as_view(), name='toaster_detail'),
    url(r'tags/$', TagListView.as_view(), name='tags'),
    url(r'^tags/(?P<slug>[-\w]+)/$', TagDetailView.as_view(), name='tag_detail'),
]