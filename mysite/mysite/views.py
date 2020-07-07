#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response

def home(request):
    context = {}
    return render_to_response('home.html',context)