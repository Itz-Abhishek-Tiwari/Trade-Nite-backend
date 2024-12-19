from .models import Category, Product, Order, Cart
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import (
    CategorySerializer,
    CartSerializer,
    ProductSerializer,
    OrderSerializer,
)


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(slef, request):
        data = request.data
        serializer = ProductSerializer(data=data)

        if not serializer.is_valid():
            return Response()

