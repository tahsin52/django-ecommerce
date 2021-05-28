from django.contrib import admin
from .models import *


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ['product', 'user', 'payment', 'product_price']
    extra = 0


admin.site.register(OrderProduct)
