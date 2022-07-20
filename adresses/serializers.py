from django.shortcuts import get_object_or_404
from rest_framework import serializers
from users.models import User

from .models import Address


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']
        read_only_fields = ['id', 'name']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "cep", "street", "number", "district", "complement", "state", "user"]
        read_only_fields = ["id"]

        def create(self, validated_data: dict):
            user_data = validated_data["user"]
            user = get_object_or_404(User, pk=user_data)
            address = Address.objects.create(**validated_data, user=user)
            user.adresses.add(address)
            return address


class AddressReadSerializer(serializers.ModelSerializer):
    user = UserAddressSerializer(read_only=True)

    class Meta:
        model = Address
        fields = ["id", "cep", "street", "number", "district", "complement", "state", "user"]
        read_only_fields = ["id"]

        def create(self, validated_data: dict):
            user_data = validated_data["user"]
            user = get_object_or_404(User, pk=user_data)
            address = Address.objects.create(**validated_data, user=user)
            user.adresses.add(address)
            return address
