from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from product.forms import ReviewForm
from django.urls import reverse_lazy
# Create your views here.


class ShopListView(ListView):
    template_name = 'shop-left-sidebar.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3

def compare(request):
    return render(request, 'compare.html')

def shopleftsidebar(request):
    products = Product.objects.all()

    context = {
        'products' : products,
    }
    return render(request, 'shop-left-sidebar.html', context)


class ShopDetailView(DetailView, FormMixin):
    form_class = ReviewForm
    model = Product
    template_name = 'single-product.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        product = self.get_object()
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.product = product
            form.save()    
        return self.get(request, *args, **kwargs)


def singleproduct(request, pk):
    product = get_object_or_404(Product, pk = pk)
    products = Product.objects.all()
    info = getattr(product, "info", None)
    context = {
        'product' : product,
        'products' : products,
        'info' : info
    }
    return render(request, 'single-product.html', context)
