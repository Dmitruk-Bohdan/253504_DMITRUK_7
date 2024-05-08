from django.urls import path, re_path
from . import views
# from django.conf.urls import url


# urlpatterns = [

#     path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('categories/', views.CategoriesListView.as_view(), name='categories'),
    re_path(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),
    re_path(r'^categoty/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category_detail'),
    path('about', views.about, name='about'),
    path('supplier/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('order_create/<int:product_id>/', views.order_create, name='order_create'),
    path('redirect-to-previous/', views.redirect_to_previous, name='redirect_to_previous'),
]
