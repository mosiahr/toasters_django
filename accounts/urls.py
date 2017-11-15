#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import logout, LoginView, RegisterView


urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^register/', RegisterView.as_view(), name='register'),
]



