from django.urls import path
from .import views

urlpatterns = [
    path('', views.homePage, name='main-home'),
    path('products/', views.products, name='main-products'),
]
