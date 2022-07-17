from attr import fields
from django.utils import timezone
from rest_framework import serializers
from django.forms import ValidationError

from .models import User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        read_only_fields = ['id']
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create(**validated_data)