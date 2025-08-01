from rest_framework import generics
from .models import Users
from .serializers import UsersSerializer
# Create your views here.

class UsersListView(generics.ListAPIView):
  queryset = Users.objects.all()
  serializer_class = UsersSerializer