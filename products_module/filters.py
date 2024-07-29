import django_filters
from .models import *
from django import forms


class ProductFilter(django_filters.FilterSet):
    weight = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class':'js-range-slider mb-3'})
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Product_categorys.objects.all(),
        widget=forms.Select(attrs={'class':'form-select mb-3'})
    )
    price = django_filters.NumberFilter(
        label='قیمت(بدون اعمال تخفیف)',
        widget=forms.NumberInput(attrs={'class':'js-range-slider mb-3'})
    )
    score = django_filters.RangeFilter(
        widget=forms.NumberInput(attrs={'class':'js-range-slider irs-hidden-input mb-3'})
    )
    discount = django_filters.RangeFilter(
        widget=forms.NumberInput(attrs={'class':'js-range-slider irs-hidden-input mb-3'})
    )
    diet = django_filters.BooleanFilter(
        widget=forms.CheckboxInput(attrs={'class':'form-check-input mb-3'})
    )
    size_box = django_filters.ChoiceFilter(
        choices = Product.list_choice,
        widget=forms.Select(attrs={'class':'form-select mb-3'})
    )

    class Meta:
        model = Product
        fields = ['category','weight','price','score','discount','diet','size_box']
