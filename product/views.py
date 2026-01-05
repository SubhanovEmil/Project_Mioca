from django.shortcuts import render
from .models import Product

# Create your views here.

def compare(request):
    return render(request, 'compare.html')

def shopleftsidebar(request):
    products = Product.objects.all()

    context = {
        'products' : products
    }
    return render(request, 'shop-left-sidebar.html', context)
    
def singleproduct(request):
    return render(request, 'single-product.html')