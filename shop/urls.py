from django.urls import path

from shop import views
from shop.apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path('products/list/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('category/list/', views.category_list, name='category_list'),
    path('category/<int:id>/', views.category_detail, name='category_detail'),
]
