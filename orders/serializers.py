# serializers.py

from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderItem
    fields = ['id', 'product_name', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
      model = Order
      fields = ['id', 'customer_name', 'phone_number', 'address', 'summa', 'deliver', 'created_at', 'items', 'status']

    def create(self, validated_data):
      items_data = validated_data.pop('items')
      order = Order.objects.create(**validated_data)
      for item in items_data:
        OrderItem.objects.create(order=order, **item)
      return order

    def update(self, instance, validated_data):
      items_data = validated_data.pop('items')
      
      # обновление полей заказа
      instance.customer_name = validated_data.get('customer_name', instance.customer_name)
      instance.phone_number = validated_data.get('phone_number', instance.phone_number)
      instance.address = validated_data.get('address', instance.address)
      instance.summa = validated_data.get('summa', instance.summa)
      instance.status = validated_data.get('status', instance.status)
      instance.deliver = validated_data.get('deliver', instance.deliver)
      instance.save()

      # удалим старые товары
      instance.items.all().delete()

      # добавим новые товары
      for item_data in items_data:
          OrderItem.objects.create(order=instance, **item_data)

      return instance 