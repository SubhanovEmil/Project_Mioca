from django.db import models
from core.models import AbstractModel
# Create your models here.

class ProductTag(AbstractModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class ProductCategory(AbstractModel):
    title = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.title
    
class Product(AbstractModel):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    tags = models.ManyToManyField(ProductTag, related_name='products')
    category = models.ForeignKey(ProductCategory, related_name = 'products', on_delete= models.CASCADE)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='product_images/', null=True, blank=True)


    def __call__(self):
        return f"{self.category.title}/{self.title}"
    
class ProductImage(AbstractModel):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title