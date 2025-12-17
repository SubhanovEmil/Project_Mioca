from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'index.html')

def error(request):
    return render(request,'404.html')

def about(request):
    return render(request,'about.html')

def blogsingle(request):
    return render(request,'blog-single.html')

def contact(request):
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')