from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login.html')

def myaccount(request):
    return render(request, 'my-account.html')

def wishlist(request):
    return render(request, 'wishlist.html')