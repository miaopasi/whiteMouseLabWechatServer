# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Shop
from django.template import loader
from django.http import Http404



class IndexView(generic.ListView):
	template_name = 'BlackList/index.html'
	context_object_name = 'latest_shop_list'

	def get_queryset(self):

		"""Return the last five published questions."""
		return Shop.objects.order_by('-update_date')[:5]
#
# def index(request):
#     # latest_shop_list = Shop.objects.order_by('-update_date')[:5]
#     # output = ', '.join([s.shop_name for s in latest_shop_list])
#     # return HttpResponse(output)
#     latest_shop_list = Shop.objects.order_by('-update_date')[:5]
#     template = loader.get_template('BlackList/index.html')
#     context = {
#         'latest_shop_list': latest_shop_list,
#     }
#     return HttpResponse(template.render(context, request))
#
#
def detail(request, shop_id):
    try:
        shop = Shop.objects.get(pk=shop_id)
    except Shop.DoesNotExist:
        raise Http404("Shop does not exist")
    return render(request, 'BlackList/detail.html', {'shop': shop})