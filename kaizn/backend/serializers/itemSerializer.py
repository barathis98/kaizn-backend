from rest_framework import serializers
from ..models import Item, Category, Tag
from .tagSerializer import TagSerializer

class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(write_only=True, allow_blank=False, source='category.name')
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Item
        fields = ['SKU', 'name', 'category_name', 'cost', 'is_assembly', 'is_component', 'is_purchaseable', 'is_salable', 'is_bundle', 'tags']
        # Note: 'category' is not directly in fields because we use 'category_name' to handle it

    def create(self, validated_data):
        # Extract and remove the category name from validated_data
        category_name = validated_data.pop('category')['name']
        # Find or create the category by name
        category, _ = Category.objects.get_or_create(name=category_name)
        validated_data['category'] = category

        # Handle tags similarly if needed
        tags_data = validated_data.pop('tags', [])
        item = Item.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            item.tags.add(tag)

        return item

    def update(self, instance, validated_data):
        category_name = validated_data.pop('category')['name']
        category, _ = Category.objects.get_or_create(name=category_name)
        instance.category = category


        instance.save()
        return instance
