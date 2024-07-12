import json
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from confluent_kafka import Producer
from .serializers import ProductSerializer
from django.conf import settings

conf = {'bootstrap.servers': settings.KAFKA_URL}
producer = Producer(**conf)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductQuantityView(APIView):
    def post(self, request, pk, format=None):
        quantity = request.data.get('quantity', None)

        if quantity is not None:
            message = {
                'product_id': pk,
                'quantity': quantity
            }
            producer.produce('product_updates', value=json.dumps(message).encode('utf-8'))
            producer.flush()
            return Response({'status': 'update enqueued'}, status=status.HTTP_200_OK)
        return Response({'error': 'invalid input'}, status=status.HTTP_400_BAD_REQUEST)
