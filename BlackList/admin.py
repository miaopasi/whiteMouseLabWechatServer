# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Shop,Comment

class ShopAdmin(admin.ModelAdmin):
    fields = ['update_date', 'shop_name']
    list_display = ('shop_name', 'update_date', 'was_update_recently')

admin.site.register(Shop, ShopAdmin)
admin.site.register(Comment)