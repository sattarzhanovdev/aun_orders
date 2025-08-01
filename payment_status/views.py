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
        data = request.data

        if not isinstance(data, list):
            return Response({"error": "Expected a list"}, status=400)

        saved, skipped = 0, 0
        for item in data:
            try:
                PaymentStatus.objects.create(
                    requestId=item.get("transactionId"),
                    timestamp=item.get("transactionDate"),
                    status=item.get("status"),
                    amount=item.get("amount"),
                    paymentMethod=item.get("transactionType")
                )
                saved += 1
            except IntegrityError:
                skipped += 1

        return Response({
            "message": "Saved",
            "saved": saved,
            "skipped_due_to_duplicate": skipped
        }, status=201)

class PaymentsCreateView(generics.CreateAPIView):
    queryset = PaymentStatus.objects.all()
    serializer_class = PaymentStatusSerializer
    
class PaymentDetailView(RetrieveAPIView):
  queryset = PaymentStatus.objects.all()
  serializer_class = PaymentStatusSerializer
  lookup_field = 'requestId'  # 👈 ищем не по pk, а по requestId
  
  

