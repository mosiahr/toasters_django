#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
#from django.contrib.auth.views import LogoutView

from .views import (
    AccountHomeView,
    AccountActivateView,
  #  AccountEmailActivateView,
    LoginView,
    RegisterView,
    AppLogoutView,
    UserDetailUpdateView,
    UserPasswordChangeView,
)


urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', AppLogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        AccountActivateView.as_view(), name='activate'),
    url(r'^password/$', UserPasswordChangeView.as_view(), name='change_password'),

    url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
]

