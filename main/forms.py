# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:56:37 2020

@author: hazac
"""

from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
    

