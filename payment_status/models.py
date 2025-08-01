from django.db import models

# Create your models here.
class PaymentStatus(models.Model):
  requestId = models.CharField(max_length=255, unique=True)
  timestamp = models.CharField(max_length=255)
  status = models.TextField()
  amount = models.FloatField()
  paymentMethod = models.CharField()

  def __str__(self):
      return f'{self.requestId} {self.status}'