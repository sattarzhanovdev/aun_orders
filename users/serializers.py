from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = ['id', 'name', 'surname', 'phone_number', 'login', 'password']

