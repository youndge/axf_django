#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Youndge
# Instructions:

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('market/', views.market, name = 'market'),
    path('cart/', views.cart, name = 'cart'),
    path('mine/', views.mine, name = 'mine'),
]

app_name = 'axf_app'