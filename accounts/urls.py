#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from accounts.views import login, logout, register

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^register/', register, name='register'),
]



