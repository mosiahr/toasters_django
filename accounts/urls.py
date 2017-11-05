#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from accounts.views import login, logout

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),

]
