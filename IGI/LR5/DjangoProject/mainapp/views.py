from datetime import datetime, timezone
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.views import View, generic
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    products = Product.objects.all()
    num_products=products.count()
    return render(
        request,
        'index.html',
        context={'num_products' : num_products,'products' : products},
    )


def about(request):
    return render(request, 'about.html')

def order_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product 
            order.date = datetime.now()
            order.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'order_create.html', context)


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

class PickupPointDetailView(generic.DetailView):
    model = PickupPoint
    context_object_name = 'pickup_point'
    template_name = 'pickup_point_detail.html'
    
class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category_detail.html'

class SupplierDetailView(generic.DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    context_object_name = 'supplier'
    paginate_by = 10
    
def redirect_to_previous(request):
    next_url = request.META.get('HTTP_REFERER')
    if next_url:
        return redirect(next_url)
    else:
        return redirect('') 

class ReviewsView():
    pass

class PurchaseView():
    pass

class PickupPointsView():
    pass
