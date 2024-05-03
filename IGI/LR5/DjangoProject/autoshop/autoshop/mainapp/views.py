from django.shortcuts import render
from .models import *
from django.views import generic

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    products = Product.objects.all()
    num_products=products.count()
    sales = Sale.objects.all()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_products' : num_products,'products' : products, 'sales': sales},
    )


def about(request):
    return render(request, 'about.html')

class NewsView(generic.ListView):
    pass

class FAQView():
    pass

class ContactsView():
    pass

class PrivacyPolicyView():
    pass

class VacanciesView():
    pass

class PromocodeView():
    pass

class SalesView():
    pass

class SuppliersView():
    pass

class ProductsListView(generic.ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    def get_queryset(self):
        return Product.objects.all()

class ProductDetailView(generic.DetailView):
    """Generic class-based detail view for a product."""
    model = Product


class ReviewsView():
    pass

class PurchaseView():
    pass

class PickupPointsView():
    pass
