from django.shortcuts import render

# Create your views here.

def compare(request):
    return render(request, 'compare.html')

def shopleftsidebar(request):
    return render(request, 'shop-left-sidebar.html')

def singleproduct(request):
    return render(request, 'single-product.html')