from .models import Category, Product, Order, Cart
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"


class CategorySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Category


class ProductSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Product


class OrderSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Order


class CartSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Cart
