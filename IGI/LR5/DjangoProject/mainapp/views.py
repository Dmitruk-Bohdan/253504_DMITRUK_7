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
from django.db.models import Q

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

def redirect_to_previous(request):
    next_url = request.META.get('HTTP_REFERER')
    if next_url:
        return redirect(next_url)
    else:
        return redirect('') 
    
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
            if user.profile.phone_number is None or user.profile.birth_date is None:
                return render(request, 'registration/register.html', {'form': form})
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
class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
        
@method_decorator(login_required, name='dispatch')
class OrderListView(generic.ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    paginate_by = 5
    
    def get_queryset(self):
        return Order.objects.all()

    def get(self, request, **kwargs):
        form = OrderSearchForm(request.GET)
        orders = Order.objects.all()
        return render(request, 'order_list.html', {'form': form, 'orders' : orders})

    def post(self, request, *args, **kwargs):
        orders = []
        form = OrderSearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            
            orders = Order.objects.filter(
                Q(customer__icontains=search_term) | Q(product__name__icontains=search_term)
            )
            
            if sort_by:
                order_by_field = sort_by if not reverse else '-' + sort_by
                orders = orders.order_by(order_by_field)
            
            orders = orders.distinct()
            
            print(orders)

            if not orders.exists():
                orders = Order.objects.all()
        else:
            form = OrderSearchForm()
            
        context = {
                'form': form,
                'orders': orders if self.request.user.is_staff else orders.filter(customer=self.request.user.username)
            }    
        return render(request, 'order_list.html', context)




@method_decorator(login_required, name='dispatch')
class PickupPointDetailView(generic.DetailView):
    model = PickupPoint
    context_object_name = 'pickup_point'
    template_name = 'pickup_point_detail.html'

@method_decorator(staff_member_required, name='dispatch')
class PickupPointListView(generic.ListView):
    model = PickupPoint
    template_name = 'pickup_point_list.html'
    context_object_name = 'pickup_points'
    paginate_by = 5
    
    def get_queryset(self):
        return PickupPoint.objects.all()

    def get(self, request, **kwargs):
        form = NameAddressForm(request.GET)
        pickup_points = PickupPoint.objects.all()
        return render(request, 'pickup_point_list.html', {'form': form, 'pickup_points' : pickup_points})

    def post(self, request, *args, **kwargs):
        pickup_points = []
        form = NameAddressForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            pickup_points = PickupPoint.objects.filter(Q(name__icontains=search_term) 
                                                    | Q(address__icontains=search_term)
                                                    | Q(phone_number__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by )
            if not pickup_points.exists():
                pickup_points = PickupPoint.objects.all()
        else:
            form = NameAddressForm()
            
        context = {
                'form': form,
                'pickup_points': pickup_points,
            }    
        return render(request, 'pickup_point_list.html', context)



class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
    
class ProductsListView(generic.ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 5
    
    def get_queryset(self):
        return Product.objects.all()

    def get(self, request, **kwargs):
        form = ProductSearchForm(request.GET)
        products = Product.objects.all()
        return render(request, 'product_list.html', {'form': form, 'products' : products})

    def post(self, request, *args, **kwargs):
        products = []
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            products = Product.objects.filter(Q(name__icontains=search_term) 
                                            | Q(article_number__icontains=search_term)
                                            | Q(description__icontains=search_term)
                                            | Q(price_per_unit__icontains=search_term)
                                            | Q(description__icontains=search_term)
                                            | Q(suppliers__name__icontains=search_term)
                                            | Q(manufacturer__name__icontains=search_term)
                                            | Q(pickup_points__name__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by ).distinct()
            print(products)
            if not products.exists():
                products = Product.objects.all()
                
        else:
            form = ProductSearchForm()
            
        context = {
                'form': form,
                'products': products,
            }    
        return render(request, 'product_list.html', context)
    
    

@method_decorator(login_required, name='dispatch')
class PromoCodeDetailView(generic.DetailView):
    model = PromoCode
    template_name = 'promocode_detail.html'
    context_object_name = 'promocode'

@method_decorator(login_required, name='dispatch')
class PromoCodeListView(generic.ListView):
    model = PromoCode
    template_name = 'promocode_list.html'
    context_object_name = 'promocodes'
    paginate_by = 5
    
    def get_queryset(self):
        return PromoCode.objects.all()

    def get(self, request, **kwargs):
        form = PromoCodeSearchForm(request.GET)
        promocodes = PromoCode.objects.all()
        return render(request, 'promocode_list.html', {'form': form, 'promocodes' : promocodes})

    def post(self, request, *args, **kwargs):
        promocodes = []
        form = PromoCodeSearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            promocodes = PromoCode.objects.filter(Q(name__icontains=search_term) 
                                                | Q(description__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by )
            if not promocodes.exists():
                promocodes = PromoCode.objects.all()
        else:
            form = PromoCodeSearchForm()
            
        context = {
                'form': form,
                'promocodes': promocodes,
            }    
        return render(request, 'promocode_list.html', context)


    
class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category_detail.html'

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 5
    
    def get_queryset(self):
        return Category.objects.all()

    def get(self, request, **kwargs):
        form = CategorySearchForm(request.GET)
        categories = Category.objects.all()
        return render(request, 'category_list.html', {'form': form, 'categories' : categories})

    def post(self, request, *args, **kwargs):
        categories = []
        form = CategorySearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            categories = Category.objects.filter(Q(name__icontains=search_term) 
                                                | Q(description__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by )
            if not categories.exists():
                categories = Category.objects.all()
        else:
            form = CategorySearchForm()
            
        context = {
                'form': form,
                'categories': categories,
            }    
        return render(request, 'category_list.html', context)



@method_decorator(staff_member_required, name='dispatch')
class ManufacturerDetailView(generic.DetailView):
    model = Manufacturer
    template_name = 'manufacturer_detail.html'
    context_object_name = 'manufacturer'

@method_decorator(staff_member_required, name='dispatch')
class ManufacturerListView(generic.ListView):
    model = Manufacturer
    template_name = 'manufacturer_list.html'
    context_object_name = 'manufacturers'
    paginate_by = 5
    
    def get_queryset(self):
        return Manufacturer.objects.all()

    def get(self, request, **kwargs):
        form = NameAddressForm(request.GET)
        manufacturers = Manufacturer.objects.all()
        return render(request, 'manufacturer_list.html', {'form': form, 'manufacturers' : manufacturers})

    def post(self, request, *args, **kwargs):
        manufacturers = []
        form = NameAddressForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            manufacturers = Manufacturer.objects.filter(Q(name__icontains=search_term) 
                                                    | Q(address__icontains=search_term)
                                                    | Q(phone__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by )
            if not manufacturers.exists():
                manufacturers = Manufacturer.objects.all()
        else:
            form = NameAddressForm()
            
        context = {
                'form': form,
                'manufacturers': manufacturers,
            }    
        return render(request, 'manufacturer_list.html', context)
        


@method_decorator(staff_member_required, name='dispatch')
class SupplierDetailView(generic.DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    context_object_name = 'supplier'
    paginate_by = 10

@method_decorator(staff_member_required, name='dispatch')
class SupplierListView(generic.ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 5
    
    def get_queryset(self):
        return Supplier.objects.all()

    def get(self, request, **kwargs):
        form = NameAddressForm(request.GET)
        suppliers = Supplier.objects.all()
        return render(request, 'supplier_list.html', {'form': form, 'suppliers' : suppliers})

    def post(self, request, *args, **kwargs):
        suppliers = []
        form = NameAddressForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            suppliers = Supplier.objects.filter(Q(name__icontains=search_term) 
                                                    | Q(address__icontains=search_term)
                                                    | Q(phone__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by )
            if not suppliers.exists():
                suppliers = Supplier.objects.all()
        else:
            form = NameAddressForm()
            
        context = {
                'form': form,
                'suppliers': suppliers,
            }    
        return render(request, 'supplier_list.html', context)

    



