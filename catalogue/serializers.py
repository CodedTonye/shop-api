from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'sku']


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']