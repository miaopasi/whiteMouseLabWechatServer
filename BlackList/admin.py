# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Shop,Comment

class ShopAdmin(admin.ModelAdmin):
    fields = ['update_date', 'shop_name','shop_id',	'avg_stars','avg_price','address', 'telephone'];
    list_display = ('shop_name', 'shop_id',	'avg_stars','avg_price','address', 'telephone','update_date', 'was_update_recently');
    search_fields = ('shop_name', 'shop_id')   #添加快速查询栏

admin.site.register(Shop, ShopAdmin)
admin.site.register(Comment)