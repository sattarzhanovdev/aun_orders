from django.shortcuts import render
from rest_framework import generics
from .models import PaymentStatus
from .serializers import PaymentStatusSerializer

# Create your views here.
class PaymentsView(generics.ListAPIView):
  queryset = PaymentStatus.objects.all()
  serializer_class = PaymentStatusSerializer