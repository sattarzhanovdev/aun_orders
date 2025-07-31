# views.py

from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderCreateView(generics.CreateAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer

class OrderListView(generics.ListAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer
  
class OrderDetailUpdateView(generics.RetrieveUpdateAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer