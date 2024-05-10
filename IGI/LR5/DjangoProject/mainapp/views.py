from datetime import datetime, timezone
from django.forms import ValidationError
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.views import View, generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    
    return render(
        request,
        'index.html',
        context={'type_request' : type(request)},
    )
    
def about(request):
    return render(request, 'about.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')
    
class HomePageView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user_timezone = self.request.session.get('django_timezone')
        
        current_datetime = datetime.now().astimezone(timezone=user_timezone)
        context['current_datetime'] = current_datetime.strftime('%d/%m/%Y')
        
        data_modified_datetime = timezone.localtime(self.model.objects.latest('modified')).strftime('%d/%m/%Y')
        context['data_modified_datetime'] = data_modified_datetime
        
        data_modified_utc = timezone.localtime(self.model.objects.latest('modified')).strftime('%d/%m/%Y')
        context['data_modified_utc'] = data_modified_utc
        
        return context


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.phone_number = form.clean_phone_number()
            user.profile.birth_date = form.clean_birth_date()
            user.profile.save()
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

@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class PromoCodeListView(generic.ListView):
    model = PromoCode
    template_name = 'promocode_list.html'
    context_object_name = 'promocodes'
    paginate_by = 5

@method_decorator(login_required, name='dispatch')
class PromoCodeDetailView(generic.DetailView):
    model = PromoCode
    template_name = 'promocode_detail.html'
    context_object_name = 'promocode'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'

@method_decorator(login_required, name='dispatch')
class PickupPointDetailView(generic.DetailView):
    model = PickupPoint
    context_object_name = 'pickup_point'
    template_name = 'pickup_point_detail.html'
    
class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category_detail.html'

@method_decorator(login_required, name='dispatch')
class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_detail.html'

@method_decorator(staff_member_required, name='dispatch')
class SupplierDetailView(generic.DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    context_object_name = 'supplier'
    paginate_by = 10

@method_decorator(staff_member_required, name='dispatch')
class ManufacturerListView(generic.ListView):
    model = Manufacturer
    template_name = 'manufacturer_list.html'
    context_object_name = 'manufacturers'
    paginate_by = 10

@method_decorator(staff_member_required, name='dispatch')
class SupplierListView(generic.ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

@method_decorator(staff_member_required, name='dispatch')
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


