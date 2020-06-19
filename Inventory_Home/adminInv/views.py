# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request,'adminInv/login.html')
def register(request):
    return render(request,'adminInv/register.html')
