from django.shortcuts import render,redirect
from product.models import Product, ProductCategory
from core.forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  django.views.generic import CreateView
# Create your views here.

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')   
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Success!")
        return super().form_valid(form)

def homepage(request):
    categories = ProductCategory.objects.all() 
    products = Product.objects.all()            
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'index.html', context)

def error(request):
    return render(request,'404.html')

def about(request):
    return render(request,'about.html')

def blogsingle(request):
    return render(request,'blog-single.html')

@login_required(login_url='login')
def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(data = request.POST) 
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Success!")
            return redirect(reverse_lazy('contact'))
    context = {'form' : form}

    return render(request,'contact.html', context)

def faq(request):
    return render(request,'faq.html')