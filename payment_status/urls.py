from django.urls import path
from .views import PaymentsView, PaymentDetailView

urlpatterns = [
  path('payments/', PaymentsView.as_view()),
  path('payments/<str:requestId>/', PaymentDetailView.as_view()),   # GET по requestId
  # path('payments/create/', PaymentsCreateView.as_view()),
]