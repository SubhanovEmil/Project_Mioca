
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from order.views import cart, checkout, emptycart, update_item

urlpatterns = [
    path('update-item/', update_item, name= 'update_item'),
    path('cart/', cart, name = 'cart'),
    path('checkout/', checkout, name = 'checkout'),
    path('empty-cart/', emptycart, name = 'empty-cart'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)