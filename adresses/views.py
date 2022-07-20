from django.shortcuts import render
from rest_framework import generics

from adresses.serializers import AddressReadSerializer, AddressSerializer

from .models import Address

# class RetrieveUpdateDestroyAddressUserView(generics.ListAPIView):
#      queryset = Address.objects.all()
#      serializer_class = AddressSerializer
#      lookup_url_kwarg = "user_id"

class CreateAddressView(generics.CreateAPIView):
     queryset = Address.objects.all()
     serializer_class = AddressSerializer

class ListAllAdressesView(generics.ListAPIView):
     queryset = Address.objects.all()
     serializer_class = AddressReadSerializer

class RetrieveUpdateDestroyAddressView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Address.objects.all()
     serializer_class = AddressSerializer

     lookup_url_kwarg = "address_id"
