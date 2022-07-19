import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .utils import CustomUserManager


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )

    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)

    

    current_banking = models.FloatField(default=0)
    agency = models.CharField(max_length=100)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    username = None
    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()
