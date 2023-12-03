from django.contrib import admin
from products.models import Basket, Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'quantity',
        'category',
    )
    fields = (
        'name',
        'description',
        ('price',
         'quantity'),
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
    ordering = ('-name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )
    list_filter = (
        'name',
    )


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = (
        'products',
        'quantity',
    )
    readonly_fields = (
        'created_timestamp',
    )
    extra = 0
