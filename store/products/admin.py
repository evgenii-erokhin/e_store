from django.contrib import admin
from products.models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
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


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )
    list_filter = (
        'name',
    )
