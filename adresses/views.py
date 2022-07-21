from django.shortcuts import render
from rest_framework import generics
from users.permissions import isSuperUser, isSuperUserOrOwner

from adresses.serializers import AddressReadSerializer, AddressSerializer

from .models import Address


class CreateAddressView(generics.CreateAPIView):
     permission_classes = [isSuperUserOrOwner]

     queryset = Address.objects.all()
     serializer_class = AddressSerializer


class ListAllAdressesView(generics.ListAPIView):
     permission_classes = [isSuperUser]

     queryset = Address.objects.all()
     serializer_class = AddressReadSerializer


class RetrieveUpdateDestroyAddressView(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [isSuperUserOrOwner]

     queryset = Address.objects.all()
     serializer_class = AddressSerializer

     lookup_url_kwarg = "address_id"
