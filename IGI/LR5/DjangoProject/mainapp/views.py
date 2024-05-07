from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import *
from django.views import View, generic

def index(request):
    products = Product.objects.all()
    num_products=products.count()
    sales = Sale.objects.all()
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
    paginate_by = 5
    def get_queryset(self):
        return Product.objects.all()

class CategoriesListView(generic.ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 5
    def get_queryset(self):
        return Category.objects.all()

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
    
class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category_detail.html'

    # def get(self, request, pk, *args, **kwargs):
    #     category = Category.objects.get(pk=pk)
    #     products = category.products.all
    #     context = {
    #         'category' : category,
    #         'products' : products
    #     }
    #     return render(request, 'category_detail.html', context)


    class UserRegistrationView(CreateView):

        form_class = RegistrationForm
        template_name = 'register.html'
        success_url = '/login/'



class SupplierDetailView(generic.DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    context_object_name = 'supplier'
    paginate_by = 10

class CreateOrderView(View):
    def get(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        context = {
            'product': product,
        }
        return render(request, 'create_order.html', context)

class ReviewsView():
    pass

class PurchaseView():
    pass

class PickupPointsView():
    pass
