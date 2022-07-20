from django.shortcuts import render
from rest_framework import generics
from .models import Address
from adresses.serializers import AddressSerializer
from users.models import User
from users.serializers import UserSerializer


# class RetrieveUpdateDestroyAddressUserView(generics.ListAPIView):
#      queryset = Address.objects.all()
#      serializer_class = AddressSerializer
#      lookup_url_kwarg = "user_id"

class ListAllAddressView(generics.ListAPIView):
     queryset = Address.objects.all()
     serializer_class = AddressSerializer

class CreatAddressView(generics.CreateAPIView):
     queryset = Address.objects.all()
     serializer_class = AddressSerializer


    
