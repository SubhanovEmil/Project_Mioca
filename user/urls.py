from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from user.views import login, logout, register, myaccount, wishlist, activate    

urlpatterns = [
    path('login/', login , name = 'login'),
    path('logout/', logout , name = 'logout'),
    path('my-account/', myaccount, name = 'my-account'),
    path('wishlist/', wishlist, name = 'wishlist'), 
    path('register/', register, name = 'register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        activate, name='activate'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
