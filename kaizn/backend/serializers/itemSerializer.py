from ..models import Item, Tag, Category
from .tagSerializer import TagSerializer
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination


class ItemSerializer(serializers.ModelSerializer):
    # Use SlugRelatedField for category to allow setting by name
    category_name = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all(),
        # source='category_name'
    )
    # Use TagSerializer for tags, allow creating new tags
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Item
        fields = ['SKU', 'name', 'category_name', 'cost', 'is_assembly', 'is_component', 'is_purchaseable', 'is_salable', 'is_bundle', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        print(f"Tags Data: {tags_data}")
        item = Item.objects.create(**validated_data)
        for tag_data in tags_data:
            tag_name = tag_data['name']
            tag, created = Tag.objects.get_or_create(name=tag_name)
            print(f"Tag: {tag_name}, Created: {created}")  
            item.tags.add(tag)
        return item


    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        return super().update(instance, validated_data)
