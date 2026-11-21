from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.generics import ListAPIView

# Create your views here.

class ProductListView(ListAPIView):
    queryset = Product.objects.all().filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

# class CategoryListView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_by_category(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response({"Error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)