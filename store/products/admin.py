from django.contrib import admin
from products.models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'short_description',
        'price',
        'quantity',
        'category',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
        'price',
        'category',
    )


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )
    list_filter = (
        'name'
    )


admin.site.register(Product)
admin.site.register(ProductCategory)
