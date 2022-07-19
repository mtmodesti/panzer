from rest_framework import generics

from users.serializers import UserSerializer

from .models import User


class CreateUserView(generics.CreateAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer

class ListUsersView(generics.ListAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer

class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer

     lookup_url_kwarg = "user_id"


