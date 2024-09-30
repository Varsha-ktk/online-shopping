import django_filters
from django import forms
from django_filters import CharFilter

from e_app.models import Product


class NameFilter(django_filters.FilterSet):

    product_name=CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder':'search product name','class':'form-control'}))

    class Meta:
        model=Product
        fields=('product_name',)

class BrandFilter(django_filters.FilterSet):

    brand=CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder':'search brand','class':'form-control'}))

    class Meta:
        model=Product
        fields=('brand',)