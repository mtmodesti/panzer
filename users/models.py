from django.db import models
from django.utils import timezone
import uuid

class User(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    phone = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=30)