from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from .models import PaymentStatus
from .serializers import PaymentStatusSerializer

# Create your views here.
from django.db import IntegrityError
class PaymentsView(APIView):
    def get(self, request):
        payments = PaymentStatus.objects.all().order_by('-id')
        serializer = PaymentStatusSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        item = request.data  # теперь это один объект, а не массив

        try:
            payment, created = PaymentStatus.objects.update_or_create(
                requestId=item.get("transactionId"),
                defaults={
                    "timestamp": item.get("transactionDate"),
                    "status": item.get("status"),
                    "amount": item.get("amount"),
                    "paymentMethod": item.get("transactionType")
                }
            )
            return Response({
                "message": "Created" if created else "Updated",
                "requestId": payment.requestId
            }, status=201)

        except Exception as e:
            return Response({
                "error": str(e)
            }, status=400)

class PaymentsCreateView(generics.CreateAPIView):
    queryset = PaymentStatus.objects.all()
    serializer_class = PaymentStatusSerializer
    
class PaymentDetailView(RetrieveAPIView):
  queryset = PaymentStatus.objects.all()
  serializer_class = PaymentStatusSerializer
  lookup_field = 'requestId'  # 👈 ищем не по pk, а по requestId
  
  

