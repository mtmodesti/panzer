import uuid

from django.db import models


class Address(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    cep = models.CharField(max_length=8)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    district = models.CharField(max_length=100)
    complement = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="adresses", null=True)
    

