import re
from django import forms
from .models import *
from django.core.validators import MinValueValidator
from django.contrib.auth.forms import *

class OrderForm(forms.ModelForm):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'number', 'min': '1'}),
        validators=[MinValueValidator(1)]
    )
    pickup_points = forms.ModelChoiceField(queryset=PickupPoint.objects.all(), empty_label=None)
    class Meta:
        model = Order
        fields = ['quantity', 'pickup_points']


class RegistrationForm(UserCreationForm):
    phone_number = forms.CharField(label='Phone number ', max_length=17, help_text='Format: +375(29)XXX-XX-XX')
    birth_date = forms.DateField(label='Birthdate', help_text='Format: YYYY-MM-DD')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        phone_number_pattern = re.compile(r'\+375(25|29|33)\d{7}')
        
        if not re.fullmatch(phone_number_pattern, phone_number):
            raise forms.ValidationError('Incorrect phone number format. Please use the format +375(29)XXX-XX-XX-XX')
        return phone_number


    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        today = datetime.now().date()
        min_age = today - timedelta(days=365 * 18)
        if birth_date > min_age:
            raise forms.ValidationError('You have to be older than 18')
        return birth_date
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'rating', 'text']
        

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError('Рейтинг должен быть от 1 до 5')
        return rating
    
class PickupPointCreateForm(forms.ModelForm):
    class Meta:
        model = PickupPoint
        fields = ['name', 'address', 'phone_number']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number_pattern = re.compile(r'^\+\d{12}$')
        
        if not re.fullmatch(phone_number_pattern, phone_number):
            raise forms.ValidationError('Incorrect phone number format. Please use the format +XXX(XX)XXX-XX-XX-XX')
        return phone_number
    
class PickupPointUpdateForm(forms.ModelForm):
    class Meta:
        model = PickupPoint
        fields = ['name', 'address', 'phone_number']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number_pattern = re.compile(r'^\+\d{12}$')
        
        if not re.fullmatch(phone_number_pattern, phone_number):
            raise forms.ValidationError('Incorrect phone number format. Please use the format +XXX(XX)XXX-XX-XX-XX')
        return phone_number
    
    def __init__(self, *args, **kwargs):
        initial_data = kwargs.get('initial', {})
        instance = kwargs.get('instance')
        
        if instance:
            initial_data['name'] = instance.name
            initial_data['address'] = instance.address
            initial_data['phone_number'] = instance.phone_number
        
        kwargs['initial'] = initial_data
        super().__init__(*args, **kwargs)

      
class CustomSearchForm(forms.Form):
    search_term = forms.CharField(label='Search term', max_length=100, required=False)
    reverse = forms.BooleanField(label='Reverse filtration', required=False)
    
class NameAddressForm(CustomSearchForm):
    sort_by = forms.ChoiceField(label='Sort by', required=False, choices=[('name', 'Name'), ('address', 'Address')])

class CategorySearchForm(CustomSearchForm):
    sort_by = forms.ChoiceField(label='Sort by', required=False, choices=[('name', 'Name')])
    
class ProductSearchForm(CustomSearchForm):
    sort_by = forms.ChoiceField(label='Sort by', required=False, choices=[('name', 'Name'), ('article_number', 'Article'),
                                ('price_per_unit', 'Price'), ('category__name', 'Category'),
                                ('manufacturer__name', 'Manufacturer')])

class OrderSearchForm(CustomSearchForm):
    sort_by = forms.ChoiceField(label='Sort by', required=False, choices=[('date', 'Date'), ('quantity', 'Quantity'),
                                                          ('customer', 'Customer'), ('pickup_point', 'Pickup point')])

class PromoCodeSearchForm(CustomSearchForm):
    sort_by = forms.ChoiceField(label='Sort by', required=False, choices=[('code', 'Code'), ('discount', 'Discount'),
                                                            ('expiration_date', 'Expiration'), ('max_usage', 'Max usage'),
                                                            ('used_counts', 'Used counts')])

class EmployeeSearchForm(CustomSearchForm):
    sort_by = forms.ChoiceField(label='Sort by', required=False, choices=[('first_name', 'First name'), ('last_name', 'Last name'),
                                                          ('birth_date', 'Age')])

class VacancySearchForm(CustomSearchForm):
    sort_by = forms.ChoiceField(label='Sort by', required=False, choices=[('title', 'Title'), ('salary', 'Salary'),
                                                          ('created_at', 'Publishing date')])

class NewsArticleSearchForm(CustomSearchForm):
    sort_by = forms.ChoiceField(label='Sort by', required=False, choices=[('title', 'Title'), ('created_at', 'Publishing date')])

class FAQSearchForm(CustomSearchForm):
    sort_by = forms.ChoiceField(label='Sort by', required=False, choices=[('title', 'Title'), ('question', 'Question'),
                                                          ('created_at', 'Publishing date')])

class ReviewSearchForm(CustomSearchForm):
    sort_by = forms.ChoiceField(label='Sort by', required=False, choices=[('title', 'Title'), ('created_at', 'Publishing date'),
                                                          ('rating', 'Rating')])
