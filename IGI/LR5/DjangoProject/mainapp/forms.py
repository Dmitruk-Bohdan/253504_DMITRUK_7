from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # fields = ['username', 'email', 'phone_number', 'age', 'password1', 'password2']


class OrderForm(forms.Form):
    amount = forms.IntegerField(min_value=1)


class OrderDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Confirm delete', required=True)


class PurchaseCreateForm(forms.Form):
    promo_code = forms.CharField(max_length=8, required=False)
    town = forms.CharField(max_length=50)