from django.contrib import admin
from django.urls import path
from core.views import homepage, error, about, blogsingle, contact, faq 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'home'),
    path('404/', error, name = '404'),
    path('about', about, name = 'about'),
    path('blog-single/', blogsingle, name = 'blog-single'),
    path('contact/', contact, name = 'contact'),
    path('faq/', faq, name = 'faq'),    
]