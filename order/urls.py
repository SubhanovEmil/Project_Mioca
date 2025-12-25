from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from order.views import cart, checkout, emptycart

urlpatterns = [
    path('cart/', cart, name = 'cart'),
    path('checkout/', checkout, name = 'checkout'),
    path('empty-cart/', emptycart, name = 'empty-cart'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)