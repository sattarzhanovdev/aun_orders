from django.urls import path
from .views import PaymentsView, PaymentsCreateView

urlpatterns = [
  path('payments/', PaymentsView.as_view()),
  path('payments/create/', PaymentsCreateView.as_view()),
]