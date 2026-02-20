from django import template
register = template.Library()
from product.models import ProductCategory

@register.simple_tag
def get_categories():
    return ProductCategory.objects.all()