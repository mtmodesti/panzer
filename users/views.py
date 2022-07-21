from rest_framework import generics

from users.permissions import isSuperUser, isSuperUserOrOwner
from users.serializers import UserSerializer

from .models import User


class CreateUserView(generics.CreateAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer

class ListUsersView(generics.ListAPIView):
     permission_classes = [isSuperUser]

     queryset = User.objects.all()
     serializer_class = UserSerializer

class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [isSuperUserOrOwner]

     queryset = User.objects.all()
     serializer_class = UserSerializer

     lookup_url_kwarg = "user_id"


