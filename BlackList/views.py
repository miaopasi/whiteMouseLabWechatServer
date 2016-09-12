# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Shop

def index(request):
    latest_shop_list = Shop.objects.order_by('-update_date')[:5]
    output = ', '.join([s.shop_name for s in latest_shop_list])
    return HttpResponse(output)


def detail(request, shop_id):
    response = "You're looking at the results of shop %s."
    return HttpResponse(response % shop_id)