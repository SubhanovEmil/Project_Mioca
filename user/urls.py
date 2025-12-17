from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from user.views import cart, checkout, emptycart, login, myaccount, wishlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', cart, name = 'cart'),
    path('checkout/', checkout, name = 'checkout'),
    path('empty-cart/', emptycart, name = 'empty-cart'),
    path('login/', login, name = 'login'),
    path('my-account/', myaccount, name = 'my-account'),
    path('wishlist/', wishlist, name = 'wishlist'), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
