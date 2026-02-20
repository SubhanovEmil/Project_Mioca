from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class ProductTag(AbstractModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class ProductCategory(AbstractModel):
    title = models.CharField(max_length=200)
    categoryimage = models.ImageField(upload_to='category_images/', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.title
    
    
class Product(AbstractModel):
    category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(ProductTag, related_name='products')

    title = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='product_cover_images/', null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    length = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True) 
    width  = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    height = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    materials = models.CharField(max_length=100, null=True, blank=True)
    madein = models.CharField(max_length=100, null=True, blank=True)
    isnew = models.BooleanField(default=False, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'{self.category.title} / {self.title}'
    
    class Meta:
        ordering = ("-created_at",)


class ProductImage(AbstractModel):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product.title
    

class ProductReview(AbstractModel):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)

    message = models.TextField()

    def __str__(self):
        return self.product.title
