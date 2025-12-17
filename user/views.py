from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, 'cart.html')
def checkout(request):
    return render(request, 'checkout.html')
def emptycart(request):
    return render(request, 'empty-cart.html')
def login(request):
    return render(request, 'login.html')
def myaccount(request):
    return render(request, 'my-account.html')
def wishlist(request):
    return render(request, 'wishlist.html')