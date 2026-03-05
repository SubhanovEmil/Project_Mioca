from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import compare, ShopListView, ShopDetailView

urlpatterns = [
    path('shop/', ShopListView.as_view(), name = 'shop-left-sidebar'),
    path('shop/<str:slug>/', ShopDetailView.as_view(), name = 'single-product'),
    path('compare/', compare, name = 'compare'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
