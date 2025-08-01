from django.contrib import admin
from .models import Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'surname', 'phone_number', 'login', 'password')
  search_fields = ('name', 'surname', 'phone_number', 'login')