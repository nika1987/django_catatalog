from django.urls import path

from shop import views
from shop.apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path('', views.product_list, name='index'),
    #path('', views.teat(), name='test'),
]
