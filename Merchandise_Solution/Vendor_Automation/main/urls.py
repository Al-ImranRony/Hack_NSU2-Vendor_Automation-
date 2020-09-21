from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='main-home'),
    # path('products/', views.products, name='main-products'),
]
