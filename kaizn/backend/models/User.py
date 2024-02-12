
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from djongo import models
import uuid

class User(AbstractUser):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    