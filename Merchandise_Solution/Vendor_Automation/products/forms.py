from django import forms

from .models import Product, ProductCategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'details', 'is_available',
                  'unit_price', 'product_counter']


class ProductCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        fields = ['name']
