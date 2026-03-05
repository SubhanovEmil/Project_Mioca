from rest_framework import serializers
from product.models import ProductCategory, Product, ProductTag
from core.models import Subscribe


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = [
            'email'
        ]



class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'title'
        ]

class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductTag
        fields = [
            'id',
            'title'
        ]

class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source = 'category.title')
    category = ProductCategorySerializer()
    tags = ProductTagSerializer(many = True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'description',
            'cover_image',
            'slug',
            'category',
            'tags',

        ]

class ProductCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'description',
            'cover_image',
            'slug',
            'category',
            'tags',

        ]

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        product = Product.objects.create(**validated_data)
        product.tags.set(tags)
        return product