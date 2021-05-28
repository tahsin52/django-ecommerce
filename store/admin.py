from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'is_available', 'created_date')
    prepopulated_fields = {'slug': ('product_name',)}


class VaritionAdmin(admin.ModelAdmin):
    list_display = ('product', 'varition_category', 'varition_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'is_active')


admin.site.register(Product, ProductAdmin)
admin.site.register(Varition, VaritionAdmin)
admin.site.register(ReviewRating)
