from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {

    }
]


def home(request):
    context = {
            'posts' : posts
        }
    return render(request, 'main/home.html', context)

def products(request):
    return render(request, 'main/products.html')