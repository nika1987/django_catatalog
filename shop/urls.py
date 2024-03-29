from django.urls import path

from shop import views
from shop.apps import ShopConfig
from django.conf import settings
from django.conf.urls.static import static

from shop.views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = ShopConfig.name


urlpatterns = [
                  path('', ProductListView.as_view(), name='index'),
                  path('product/<int:pk>/', ProductDetailView.as_view(), name='test'),
                  path('category/list/', CategoryListView.as_view(), name='category_list'),
                  path('category/<int:id>/', CategoryDetailView.as_view(), name='category_detail'),
                  path('product/create/', ProductCreateView.as_view(), name='create_product'),
                  path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
                  path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
