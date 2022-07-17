from django.shortcuts import render
from .models import User
from users.serializers import UserSerializer
from rest_framework.generics import CreateAPIView


class CreateUserView(CreateAPIView):

     queryset = User.objects.all()
     
     serializer_class = UserSerializer