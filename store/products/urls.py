from django.urls import path
from .views import index, products, add_to_basket


app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products_list'),
    path('baskets/add/<int:product_id>/', add_to_basket, name='add_to_baskets')
]
