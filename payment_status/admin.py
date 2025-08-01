from django.contrib import admin
from .models import PaymentStatus

@admin.register(PaymentStatus)
class PaymentsAdmin(admin.ModelAdmin):
  list_display = ['requestId', 'status', 'amount', 'paymentMethod', 'timestamp']
  search_fields = ('requestId', 'status', 'amount')