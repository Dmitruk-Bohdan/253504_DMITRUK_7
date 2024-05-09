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
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('pickup_points/', views.PickupPointListView.as_view(), name='pickup_points'),
    path('promocodes/', views.PromoCodeListView.as_view(), name='promocodes'),
    path('manufacturers/', views.ManufacturerListView.as_view(), name='manufacturers'),
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers'),
    re_path(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),
    re_path(r'^categoty/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category_detail'),
    re_path(r'^order/(?P<pk>\d+)$', views.OrderDetailView.as_view(), name='order_detail'),
    re_path(r'^promocode/(?P<pk>\d+)$', views.PromoCodeDetailView.as_view(), name='promocode_detail'),
    re_path(r'^pickup_point/(?P<pk>\d+)$', views.PickupPointDetailView.as_view(), name='pickup_point_detail'),
    re_path(r'^manufacturer/(?P<pk>\d+)$', views.ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    path('about', views.about, name='about'),
    path('supplier/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('order_create/<int:product_id>/', views.order_create, name='order_create'),
    path('redirect-to-previous/', views.redirect_to_previous, name='redirect_to_previous'),
]
