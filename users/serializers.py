from adresses.serializers import AddressSerializer
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import User


class UserSerializer(serializers.ModelSerializer):
    adresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'cpf', 'email', 'phone', 'password', 'current_banking', 'agency', 'created_at', 'updated_at', 'adresses']
        read_only_fields = ['id', 'current_banking', 'created_at', 'updated_at']

        extra_kwargs = {
            "password": {"write_only": True},
            "cpf": {"write_only": True}
        }



    def update(self, instance: User, validated_data):
        fixedFields = ['cpf']
        for key, value in validated_data.items():
            if key not in fixedFields:
                if key == 'password':
                    instance.set_password(value)
                else:
                    setattr(instance, key, value)
                # setattr(instance, key, value)
        instance.save()

        return instance
        

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
