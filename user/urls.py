from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from user.views import login, myaccount, wishlist

urlpatterns = [
    path('login/', login, name = 'login'),
    path('my-account/', myaccount, name = 'my-account'),
    path('wishlist/', wishlist, name = 'wishlist'), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
