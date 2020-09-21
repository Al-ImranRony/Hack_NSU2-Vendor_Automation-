from django import forms

from .models import Product, ProductCategory


class ProductForm(forms.ModelForm):

    category = forms.ChoiceField(widget=forms.Select,
                                 choices=ProductCategory.objects.all().values_list(),
                                 required=True)

    class Meta:
        model = Product
        fields = ['name', 'details', 'category', 'is_available',
                  'unit_price', 'product_counter']


class ProductCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        fields = ['name']
