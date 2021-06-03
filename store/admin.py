from django.contrib import admin
from .models import *
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'is_available', 'created_date')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class VaritionAdmin(admin.ModelAdmin):
    list_display = ('product', 'varition_category', 'varition_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'is_active')



admin.site.register(Product, ProductAdmin)
admin.site.register(Varition, VaritionAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
