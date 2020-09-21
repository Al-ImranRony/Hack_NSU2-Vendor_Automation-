from django.urls import path

from .views import (
    ProductCategoryCreateView,
    ProductCategoryUpdateView,
    ProductCategoryDeleteView,
    ProductCategoryDetailView,
    ProductCategoryListView,

    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView
)

urlpatterns = [
    path("category/", ProductCategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>", ProductCategoryDetailView.as_view(),
         name="category_detail"),
    path("category/new", ProductCategoryCreateView.as_view(), name="category_create"),
    path("category/<int:pk>/update",
         ProductCategoryUpdateView.as_view(), name="category_update"),
    path("category/<int:pk>/delete",
         ProductCategoryDeleteView.as_view(), name="category_delete"),

    path("category/<int:cpk>/product/",
         ProductListView.as_view(), name="product_list"),
    path("category/<int:cpk>/product/new",
         ProductCreateView.as_view(), name="product_create"),
    path("category/<int:cpk>/product/<int:pk>",
         ProductDetailView.as_view(), name="product_detail"),
    path("category/<int:cpk>/product/<int:pk>/update",
         ProductUpdateView.as_view(), name="product_update"),
    path("category/<int:cpk>/product/<int:pk>/delete",
         ProductDeleteView.as_view(), name="product_delete"),

]
