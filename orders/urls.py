from django.urls import path
from .views import OrderCreateView, OrderListView, OrderDetailUpdateView

urlpatterns = [
  path('orders/', OrderListView.as_view(), name='order-list'),
  path('orders/create/', OrderCreateView.as_view(), name='order-create'),
  path('orders/<int:pk>/', OrderDetailUpdateView.as_view(), name='order-detail-update'),
]