from django.urls import path, re_path
from . import views
# from django.conf.urls import url


# urlpatterns = [

#     path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    re_path(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),
    path('about', views.about, name='about'),
    path('supplier/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('create_order/<int:pk>/', views.CreateOrderView.as_view(), name='create_order'),
]
