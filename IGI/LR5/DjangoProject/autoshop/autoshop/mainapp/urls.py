from django.urls import path
from . import views
# from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
]

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^products/$', views.BookListView.as_view(), name='products'),
#     url(r'^product/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='product_detail'),
# ]
