# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:16:48 2020

@author: hazac
"""

from django.urls import path

from . import views

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("create/", views.create, name="create"),
path("view/", views.view, name="view"),
]
