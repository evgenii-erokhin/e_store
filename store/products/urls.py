from django.urls import path
from .views import IndexView, products, add_to_basket, basket_remove


app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', products, name='products_list'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_number>', products, name='paginator'),
    path('baskets/add/<int:product_id>/',
         add_to_basket, name='add_to_baskets'
         ),
    path('basket/remove/<int:basket_id>/',
         basket_remove, name='basket_remove'
         ),
]
