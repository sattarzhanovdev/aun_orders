from django.db import models

class Order(models.Model):
  customer_name = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=50)
  address = models.TextField()
  summa = models.FloatField()
  status = models.CharField(default='На доставку')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f'Заказ {self.id} от {self.customer_name}'


class OrderItem(models.Model):
  order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
  product_name = models.CharField(max_length=255)
  quantity = models.PositiveIntegerField(default=1)
  price = models.FloatField()

  def __str__(self):
      return f'{self.product_name} x {self.quantity}'