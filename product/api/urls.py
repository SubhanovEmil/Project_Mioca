from django.urls import path
from product.api.views import (
    categories, 
    product_update, 
    ProductListAPIView, 
    ProductUpdateDeleteAPIView,
    SubscriberAPIView,
    ProudctTagListAPIView
)
    
urlpatterns = [
    path('categories/', categories, name= 'categories'),
    path('tags/', ProudctTagListAPIView.as_view(), name = 'tags'),
    path('products/', ProductListAPIView.as_view(), name= 'products'),
    path('products/<int:pk>/', ProductUpdateDeleteAPIView.as_view(), name= 'product_update'),
    path('subscriber/', SubscriberAPIView.as_view(), name = 'subscriber' )
]