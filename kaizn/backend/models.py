# models.py
from typing import AbstractSet
# from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from djongo import models
import uuid
from djongo.models import ArrayField
from djongo.models import fields






class User(AbstractUser):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
    
# models.py

# class Tag(models.Model):
#     id = models.CharField(primary_key=True, max_length=50, unique=True)

#     name = models.CharField(max_length=50, unique=True)

class Item(models.Model):
    sku = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    stock_quantity = models.PositiveIntegerField(default=0)




