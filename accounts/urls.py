#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth.views import LogoutView

from .views import (
    AccountHomeView,
    LoginView,
    RegisterView,
)


urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]



