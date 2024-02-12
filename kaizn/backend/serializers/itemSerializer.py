from ..models import Item
from rest_framework import serializers
class ItemSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)  # Makes the description optional
    
    class Meta:
        model = Item
        fields = '__all__'
