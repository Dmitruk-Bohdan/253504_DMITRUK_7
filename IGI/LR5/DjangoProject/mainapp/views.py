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
def review_create(request, product_id):
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
            promocodes = PromoCode.objects.filter(Q(code__icontains=search_term) 
                                                | Q(discount__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by )
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



@method_decorator(login_required, name='dispatch')
class FAQDetailView(generic.DetailView):
    model = FAQ
    template_name = 'faq_detail.html'
    context_object_name = 'faq'

@method_decorator(login_required, name='dispatch')
class FAQListView(generic.DetailView):
    model = FAQ
    template_name = 'faq_list.html'
    context_object_name = 'faqs'
    paginate_by = 5

    def get_queryset(self):
        return FAQ.objects.all()

    def get(self, request, **kwargs):
        form = FAQSearchForm(request.GET)
        faqs = FAQ.objects.all()
        return render(request, 'faq_list.html', {'form': form, 'faqs' : faqs})

    def post(self, request, *args, **kwargs):
        faqs = []
        form = FAQSearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            faqs = FAQ.objects.filter(Q(title__icontains=search_term) 
                                    | Q(created_at__icontains=search_term)
                                    | Q(question__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by )
            if not faqs.exists():
                faqs = FAQ.objects.all()
        else:
            form = FAQSearchForm()
            
        context = {
                'form': form,
                'faqs': faqs,
            }    
        return render(request, 'faq_list.html', context)



@method_decorator(login_required, name='dispatch')
class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'review_detail.html'
    context_object_name = 'review'

@method_decorator(login_required, name='dispatch')
class ReviewListView(generic.DetailView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'
    paginate_by = 5

    def get_queryset(self):
        return Review.objects.all()

    def get(self, request, **kwargs):
        form = ReviewSearchForm(request.GET)
        reviews = Review.objects.all()
        return render(request, 'review_list.html', {'form': form, 'reviews' : reviews})

    def post(self, request, *args, **kwargs):
        reviews = []
        form = ReviewSearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            reviews = Review.objects.filter(Q(title__icontains=search_term) 
                                        | Q(text__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by )
            if not reviews.exists():
                reviews = Review.objects.all()
        else:
            form = ReviewSearchForm()
            
        context = {
                'form': form,
                'reviews': reviews,
            }    
        return render(request, 'review_list.html', context)





@method_decorator(login_required, name='dispatch')
class NewsArticleDetailView(generic.DetailView):
    model = NewsArticle
    template_name = 'news_article_detail.html'
    context_object_name = 'news_article'

@method_decorator(login_required, name='dispatch')
class NewsArticleListView(generic.DetailView):
    model = NewsArticle
    template_name = 'news_article_detail.html'
    context_object_name = 'news_articles'
    paginate_by = 5

    def get_queryset(self):
        return NewsArticle.objects.all()

    def get(self, request, **kwargs):
        form = NewsArticleSearchForm(request.GET)
        news_articles = NewsArticle.objects.all()
        return render(request, 'news_article_list.html', {'form': form, 'news_articles' : news_articles})

    def post(self, request, *args, **kwargs):
        news_articles = []
        form = NewsArticleSearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            news_articles = NewsArticle.objects.filter(Q(title__icontains=search_term) 
                                                    | Q(text__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by )
            if not news_articles.exists():
                news_articles = NewsArticle.objects.all()
        else:
            form = NewsArticleSearchForm()
            
        context = {
                'form': form,
                'news_articles': news_articles,
            }    
        return render(request, 'news_article_list.html', context)




@method_decorator(login_required, name='dispatch')
class AboutArticleListView(generic.DetailView):
    model = AboutArticle
    template_name = 'about_article_list.html'
    context_object_name = 'about_articles'
    pagitane_by = 5

    def get(self, request, **kwargs):
        about_articles = AboutArticle.objects.all()
        return render(request, 'about_us.html', {'about_articles' : about_articles})



@method_decorator(login_required, name='dispatch')
class VacancyDetailView(generic.DetailView):
    model = Vacancy
    template_name = 'vacancy_detail.html'
    context_object_name = 'vacancy'

@method_decorator(login_required, name='dispatch')
class VacancyListView(generic.DetailView):
    model = Vacancy
    template_name = 'vacancy_list.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.all()

    def get(self, request, **kwargs):
        form = VacancySearchForm(request.GET)
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy_list.html', {'form': form, 'vacancies' : vacancies})

    def post(self, request, *args, **kwargs):
        vacancies = []
        form = VacancySearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            vacancies = Vacancy.objects.filter(Q(title__icontains=search_term) 
                                                | Q(description__icontains=search_term)
                                                | Q(responsibilities__icontains=search_term)
                                                | Q(location__icontains=search_term)
                                                | Q(requirements__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by )
            if not vacancies.exists():
                vacancies = Vacancy.objects.all()
        else:
            form = VacancySearchForm()
            
        context = {
                'form': form,
                'vacancies': vacancies,
            }    
        return render(request, 'vacancy_list.html', context)



@method_decorator(login_required, name='dispatch')
class EmployeeListView(generic.DetailView):
    model = User
    template_name = 'employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return User.objects.all()

    def get(self, request, **kwargs):
        form = EmployeeSearchForm(request.GET)
        if self.request.user.is_staff:
            employees = User.objects.all()
        else:
            employees = User.objects.filter(profile__non_secretive=True)
        return render(request, 'employee_list.html', {'form': form, 'employees' : employees})

    def post(self, request, *args, **kwargs):
        employees = []
        form = EmployeeSearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            sort_by = form.cleaned_data.get('sort_by')
            reverse = form.cleaned_data.get('reverse')
            employees = User.objects.filter(      Q(username__icontains=search_term)
                                                | Q(email__icontains=search_term)
                                                | Q(first_name__icontains=search_term)
                                                | Q(last_name__icontains=search_term)
                                                | Q(profile__phone_number__icontains=search_term)
                                                | Q(profile__job_description__icontains=search_term)).order_by(sort_by if not reverse else '-' + sort_by ).distinct()
            if not employees.exists():
                employees = User.objects.all()
        else:
            form = EmployeeSearchForm()
            
        context = {
                'form': form,
                'employees': employees if self.request.user.is_staff else employees.filter(Q(profile__non_secretive = True))
            }    
        return render(request, 'employee_list.html', context)

