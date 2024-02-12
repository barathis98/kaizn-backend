from rest_framework import serializers
from ..models import StockItem, Item

class StockItemSerializer(serializers.ModelSerializer):
    item_sku = serializers.CharField(write_only=True)

    class Meta:
        model = StockItem
        fields = ['item_sku', 'in_stock', 'total_allocated', 'allocated_to_builds', 'allocated_to_sales', 'available_stock', 'incoming_stock', 'net_stock', 'min_stock', 'desired_stock']

    def create(self, validated_data):
        sku = validated_data.pop('item_sku')
        item = Item.objects.get(SKU=sku)  # Lookup Item by SKU
        validated_data['item'] = item
        return StockItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'item_sku' in validated_data:
            sku = validated_data.pop('item_sku')
            instance.item = Item.objects.get(SKU=sku)  # Update Item by SKU if needed
        return super().update(instance, validated_data)
