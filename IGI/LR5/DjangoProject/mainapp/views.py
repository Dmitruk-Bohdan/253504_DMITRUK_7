from datetime import datetime, timezone
from django.forms import ValidationError
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.views import View, generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate

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

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if 'is_adult' not in request.POST:
                raise ValidationError('you must be over 18 to sign up')
            user.profile.phone_number = form.clean_phone_number
            user.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def order_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user.username
            order.product = product 
            order.date = datetime.now()
            order.pickup_point = form.cleaned_data['pickup_points']
            order.save()
            return redirect('order_detail', pk=order.id)
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

class OrderListView(generic.ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    paginate_by = 5
    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(customer=self.request.user.username)
    
class PickupPointListView(generic.ListView):
    model = PickupPoint
    template_name = 'pickup_point_list.html'
    context_object_name = 'pickup_points'
    paginate_by = 5
    def get_queryset(self):
        return PickupPoint.objects.all()

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
    
class PromoCodeListView(generic.ListView):
    model = PromoCode
    template_name = 'promocode_list.html'
    context_object_name = 'promocodes'
    paginate_by = 5

class PromoCodeDetailView(generic.DetailView):
    model = PromoCode
    template_name = 'promocode_detail.html'
    context_object_name = 'promocode'

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

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_detail.html'

class SupplierDetailView(generic.DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    context_object_name = 'supplier'
    paginate_by = 10

class ManufacturerListView(generic.ListView):
    model = Manufacturer
    template_name = 'manufacturer_list.html'
    context_object_name = 'manufacturers'
    paginate_by = 10

class SupplierListView(generic.ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

class ManufacturerDetailView(generic.DetailView):
    model = Manufacturer
    template_name = 'manufacturer_detail.html'
    context_object_name = 'manufacturer'
    
def redirect_to_previous(request):
    next_url = request.META.get('HTTP_REFERER')
    if next_url:
        return redirect(next_url)
    else:
        return redirect('') 

class ReviewsView():
    pass
