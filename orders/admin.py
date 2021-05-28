from django.contrib import admin

from order_product.admin import OrderProductInline
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'order_total', 'tax', 'status']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'email']
    list_per_page = 15
    inlines = [OrderProductInline]

admin.site.register(Order, OrderAdmin)
