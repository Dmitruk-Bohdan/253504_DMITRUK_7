from django.urls import path, re_path
from . import views
# from django.conf.urls import url


# urlpatterns = [

#     path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('pickup_points/', views.PickupPointListView.as_view(), name='pickup_points'),
    path('promocodes/', views.PromoCodeListView.as_view(), name='promocodes'),
    path('manufacturers/', views.ManufacturerListView.as_view(), name='manufacturers'),
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers'),
    
    path('faqs/', views.FAQListView.as_view(), name='faqs'),
    path('news_articles/', views.NewsArticleListView.as_view(), name='news_articles'),
    path('reviews/', views.ReviewListView.as_view(), name='reviews'),
    path('vacancies/', views.VacancyListView.as_view(), name='vacancies'),
    path('employees/', views.EmployeeListView.as_view(), name='employees'),
    path('about_us', views.AboutArticleListView.as_view(), name='about_us'),
    
    re_path(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),
    re_path(r'^categoty/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category_detail'),
    re_path(r'^order/(?P<pk>\d+)$', views.OrderDetailView.as_view(), name='order_detail'),
    re_path(r'^promocode/(?P<pk>\d+)$', views.PromoCodeDetailView.as_view(), name='promocode_detail'),
    re_path(r'^pickup_point/(?P<pk>\d+)$', views.PickupPointDetailView.as_view(), name='pickup_point_detail'),
    re_path(r'^manufacturer/(?P<pk>\d+)$', views.ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    
    re_path(r'^faq/(?P<pk>\d+)$', views.FAQDetailView.as_view(), name='faq_detail'),
    re_path(r'^news_article/(?P<pk>\d+)$', views.NewsArticleDetailView.as_view(), name='news_article_detail'),
    re_path(r'^review/(?P<pk>\d+)$', views.ReviewDetailView.as_view(), name='review_detail'),
    re_path(r'^vacancy/(?P<pk>\d+)$', views.VacancyDetailView.as_view(), name='vacancy_detail'),
    
    path('about', views.about, name='about'),
    path('register', views.register_view, name='register'),
    path('supplier/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('order_create/<int:product_id>/', views.OrderCreateView.as_view(), name='order_create'),
    path('pickup_point_create/', views.PickupPointCreateView.as_view(), name='pickup_point_create'),
    path('pickup_point_update/<int:pk>/', views.PickupPointUpdateView.as_view(), name='pickup_point_update'),
    path('pickup_point/<int:pk>/delete/', views.PickupPointDeleteView.as_view(), name='pickup_point_delete'),
    path('review_create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('redirect-to-previous/', views.redirect_to_previous, name='redirect_to_previous'),
]
