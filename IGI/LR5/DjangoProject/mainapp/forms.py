from django import forms
from .models import *
from django.core.validators import MinValueValidator

class OrderForm(forms.ModelForm):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'number', 'min': '1'}),
        validators=[MinValueValidator(1)]
    )
    pickup_points = forms.ModelChoiceField(queryset=PickupPoint.objects.all(), empty_label=None)
    class Meta:
        model = Order
        fields = ['quantity', 'pickup_points']