# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	
	return render(request, 'index.html')

def base(request):
	
	return render(request, 'base.html')