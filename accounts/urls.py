#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth.views import LogoutView

from .views import (
    AccountHomeView,
    AccountActivateView,
  #  AccountEmailActivateView,
    LoginView,
    RegisterView,
)


urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
  #  url(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$',
  #          AccountEmailActivateView.as_view(),
  #          name='email-activate'),

    url(r'^activate/(?P<uid>[0-9A-Za-z]+)/$',
        AccountActivateView.as_view(), name='activate'),
]

