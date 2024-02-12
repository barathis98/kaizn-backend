from rest_framework import serializers
from ..models import StockItem

class StockItemDashboardSerializer(serializers.ModelSerializer):
    item_sku = serializers.CharField(source='item.SKU', read_only=True)
    item_name = serializers.CharField(source='item.name', read_only=True)
    category_name = serializers.CharField(source='item.category.name', read_only=True)
    tags = serializers.SerializerMethodField()

    class Meta:
        model = StockItem
        fields = ['item_sku', 'item_name', 'category_name', 'tags', 'in_stock', 'total_allocated', 'allocated_to_builds', 'allocated_to_sales', 'available_stock', 'incoming_stock', 'net_stock', 'min_stock', 'desired_stock']

    def get_tags(self, instance):
        return [tag.name for tag in instance.item.tags.all()]
