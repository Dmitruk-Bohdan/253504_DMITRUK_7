import re
from django import forms
from .models import *
from django.core.validators import MinValueValidator
from django.contrib.auth.forms import *

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

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
    # is_adult = forms.BooleanField(label='Confirm that you are over 18 years of age', required=True)

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