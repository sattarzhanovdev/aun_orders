from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
  model = OrderItem
  extra = 0

@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
  list_display = ('id', 'customer_name', 'phone_number', 'address', 'summa', 'status', 'created_at')
  search_fields = ('customer_name', 'phone_number', 'address')
  list_filter = ('status', 'created_at')
  inlines = [OrderItemInline]