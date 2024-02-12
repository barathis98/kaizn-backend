# serializers.py
from rest_framework import generics
from ..models import User, Item
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  
        extra_kwargs = {'password': {'write_only': True}}