from django.shortcuts import render


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from pprint import pprint
from datetime import datetime
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from django.views.generic.edit import FormMixin

from .models import Product, ProductCategory
from .forms import ProductForm, ProductCategoryForm

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = 'products'
    ordering = ['name']
    paginate_by = 20


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    fields = ['name', 'details', 'is_available',
              'unit_price', 'product_counter']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def form_valid(self, form):
        form.instance.vendor = self.request.user
        # form.instance.category = self.
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'details', 'is_available',
              'unit_price', 'product_counter']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def form_valid(self, form):
        form.instance.vendor = self.request.user
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product

    def test_func(self):
        product = self.get_object()

        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('product_list')


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = "products/productcategory_list.html"
    context_object_name = 'categories'
    ordering = ['name']
    paginate_by = 20


class ProductCategoryDetailView(DetailView):
    model = ProductCategory

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        category = ProductCategory.objects.filter(pk=self.kwargs.get('pk'))[0]
        context["products"] = Product.objects.filter(
            category=category).order_by('-product_counter')
        return context


class ProductCategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ProductCategory

    fields = ['name']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def form_valid(self, form):
        return super().form_valid(form)


class ProductCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProductCategory

    fields = ['name']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    def form_valid(self, form):
        return super().form_valid(form)


class ProductCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ProductCategory

    def test_func(self):
        product = self.get_object()

        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse('productcategory_list')
