from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from product.views import compare, shopleftsidebar, singleproduct

urlpatterns = [
    path('single-product', singleproduct, name = 'single-product'),
    path('compare/', compare, name = 'compare'),
    path('shop-left-sidebar/', shopleftsidebar, name = 'shop-left-sidebar'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
